use core::pin::Pin;
use disage;
use futures::Stream;
use std::io::Cursor;
use std::sync::RwLock;
use std::time::{Instant};
use stepth::*;
use stepth_service::stepth_service_server::{StepthService, StepthServiceServer};
use stepth_service::*;
use tokio::sync::mpsc;
use tonic::transport::Server;
use tonic::{Request, Response, Status};

pub mod stepth_service {
    tonic::include_proto!("stepth_service");
}

#[derive(Debug, Default)]
pub struct StepthServerInstance {
    mask_image: RwLock<MaskImage>,
    depth: RwLock<image::ImageBuffer<image::Luma<u8>, Vec<u8>>>,
}

#[tonic::async_trait]
impl StepthService for StepthServerInstance {
    async fn beep(
        &self,
        _request: Request<EmptyRequest>,
    ) -> Result<Response<StringResponse>, Status> {
        println!("Received beep!");
        Ok(Response::new(StringResponse {
            message: "beep".to_string(),
        }))
    }
    type LoadImageStream =
        Pin<Box<dyn Stream<Item = Result<ImageResponse, Status>> + Send + Sync + 'static>>;
    async fn load_image(
        &self,
        request: Request<LoadImageRequest>,
    ) -> Result<Response<Self::LoadImageStream>, Status> {
        let image_path = request.into_inner().path;
        println!("Will try to load image from path {}", image_path);
        let (tx, rx) = mpsc::channel(4);
        match image::open(image_path) {
            Ok(img) => {
                println!("Image was read");
                *self.mask_image.write().unwrap() = MaskImage::from_image(img.clone());
                tokio::spawn(async move {
                    let mut bytes: Vec<u8> = Vec::new();
                    img.write_to(&mut Cursor::new(&mut bytes), image::ImageFormat::Jpeg)
                        .unwrap();
                    for chunk in bytes.chunks(4194299) {
                        let resp = Ok(ImageResponse {
                            raw_data: chunk.to_vec(),
                        });
                        tx.send(resp).await.unwrap();
                    }
                    println!("Image was sent");
                });
                Ok(Response::new(Box::pin(
                    tokio_stream::wrappers::ReceiverStream::new(rx),
                )))
            }
            _ => Err(Status::new(tonic::Code::NotFound, "Failed to open image")),
        }
    }
    type LoadImageToCurrentStream = Self::LoadImageStream;
    async fn load_image_to_current(
        &self,
        request: Request<LoadImageRequest>,
    ) -> Result<Response<Self::LoadImageStream>, Status> {
        let image_path = request.into_inner().path;
        println!("Will try to load image from path {}", image_path);
        let (tx, rx) = mpsc::channel(4);
        match image::open(image_path) {
            Ok(img) => {
                println!("Image was read");
                self.mask_image
                    .write()
                    .unwrap()
                    .image_replace(&MaskImage::from_image(img), disage::Position::new(0, 0));
                let img =
                    image::DynamicImage::ImageRgba8(self.mask_image.read().unwrap().image.clone());
                tokio::spawn(async move {
                    let mut bytes: Vec<u8> = Vec::new();
                    img.write_to(&mut Cursor::new(&mut bytes), image::ImageFormat::Jpeg)
                        .unwrap();
                    for chunk in bytes.chunks(4194299) {
                        let resp = Ok(ImageResponse {
                            raw_data: chunk.to_vec(),
                        });
                        tx.send(resp).await.unwrap();
                    }
                    println!("Image was sent");
                });
                Ok(Response::new(Box::pin(
                    tokio_stream::wrappers::ReceiverStream::new(rx),
                )))
            }
            _ => Err(Status::new(tonic::Code::NotFound, "Failed to open image")),
        }
    }
    async fn load_depth(
        &self,
        request: Request<LoadImageRequest>,
    ) -> Result<Response<StringResponse>, Status> {
        let image_path = request.into_inner().path;
        println!("Will try to load depth from path {}", image_path);
        match image::open(image_path) {
            Ok(img) => {
                println!("Depth was read");
                *self.depth.write().unwrap() = img.to_luma8();
                Ok(Response::new(StringResponse {
                    message: "Depth was added".to_string(),
                }))
            }
            _ => Err(Status::new(tonic::Code::NotFound, "Failed to add depth")),
        }
    }

    async fn load_depth_from_additional(
        &self,
        request: Request<LoadImageRequest>,
    ) -> Result<Response<StringResponse>, Status> {
        let image_path = request.into_inner().path;
        println!("Will try to load depth from path {}", image_path);
        match image::open(image_path) {
            Ok(img) => {
                println!("Depth was read");
                let mut temp_depth =
                    DepthImage::from_image(self.mask_image.read().unwrap().image());
                let start = Instant::now();
                match temp_depth.load_depth_from_additional(img, [10; 3]) {
                    Ok(()) => {
                        let msg =
                            format!("Depth was added, time took {}s", start.elapsed().as_secs());
                        println!("{}", msg);
                        *self.depth.write().unwrap() = temp_depth.depth;
                        Ok(Response::new(StringResponse { message: msg }))
                    }
                    _ => Err(Status::new(tonic::Code::Internal, "Failed to add depth")),
                }
            }
            _ => Err(Status::new(tonic::Code::NotFound, "Failed to add depth")),
        }
    }

    type HighlightDepthStream = Self::LoadImageStream;

    async fn highlight_depth(
        &self,
        request: Request<HighlightRequest>,
    ) -> Result<Response<Self::HighlightDepthStream>, Status> {
        println!("Will highlight depth");
        let (tx, rx) = mpsc::channel(4);
        if request.into_inner().enabled {
            let mut depth_image = DepthImage::default();
            depth_image.image = self.mask_image.read().unwrap().image.clone();
            match depth_image.load_depth(self.depth.read().unwrap().clone()) {
                Ok(()) => {
                    println!("Successfully added depth");
                    let img = depth_image.highlight_depth();
                    tokio::spawn(async move {
                        let mut bytes: Vec<u8> = Vec::new();
                        img.write_to(&mut Cursor::new(&mut bytes), image::ImageFormat::Jpeg)
                            .unwrap();
                        for chunk in bytes.chunks(4194299) {
                            let resp = Ok(ImageResponse {
                                raw_data: chunk.to_vec(),
                            });
                            tx.send(resp).await.unwrap();
                        }
                        println!("Image was sent");
                    });
                    Ok(Response::new(Box::pin(
                        tokio_stream::wrappers::ReceiverStream::new(rx),
                    )))
                }
                _ => Err(Status::new(tonic::Code::Internal, "Failed to highlight")),
            }
        } else {
            let img =
                image::DynamicImage::ImageRgba8(self.mask_image.read().unwrap().image.clone());
            tokio::spawn(async move {
                let mut bytes: Vec<u8> = Vec::new();
                img.write_to(&mut Cursor::new(&mut bytes), image::ImageFormat::Jpeg)
                    .unwrap();
                for chunk in bytes.chunks(4194299) {
                    let resp = Ok(ImageResponse {
                        raw_data: chunk.to_vec(),
                    });
                    tx.send(resp).await.unwrap();
                }
                println!("Image was sent");
            });
            Ok(Response::new(Box::pin(
                tokio_stream::wrappers::ReceiverStream::new(rx),
            )))
        }
    }

    async fn invert_depth(
        &self,
        _request: Request<EmptyRequest>,
    ) -> Result<Response<StringResponse>, Status> {
        println!("Received invert depth!");
        let mut temp_depth = DepthImage::from_image(self.mask_image.read().unwrap().image());
        temp_depth.depth = self.depth.read().unwrap().clone();
        temp_depth.invert_depth();
        *self.depth.write().unwrap() = temp_depth.depth;
        Ok(Response::new(StringResponse {
            message: "Inverted".to_string(),
        }))
    }

    type HighlightMaskStream = Self::LoadImageStream;

    async fn highlight_mask(
        &self,
        request: Request<HighlightRequest>,
    ) -> Result<Response<Self::HighlightDepthStream>, Status> {
        println!("Will highlight mask");
        let (tx, rx) = mpsc::channel(4);
        let img = if request.into_inner().enabled {
            self.mask_image.read().unwrap().highlight_mask()
        } else {
            image::DynamicImage::ImageRgba8(self.mask_image.read().unwrap().image.clone())
        };
        tokio::spawn(async move {
            let mut bytes: Vec<u8> = Vec::new();
            img.write_to(&mut Cursor::new(&mut bytes), image::ImageFormat::Jpeg)
                .unwrap();
            for chunk in bytes.chunks(4194299) {
                let resp = Ok(ImageResponse {
                    raw_data: chunk.to_vec(),
                });
                tx.send(resp).await.unwrap();
            }
            println!("Image was sent");
        });
        Ok(Response::new(Box::pin(
            tokio_stream::wrappers::ReceiverStream::new(rx),
        )))
    }

    async fn invert_mask(
        &self,
        _request: Request<EmptyRequest>,
    ) -> Result<Response<StringResponse>, Status> {
        println!("Received invert mask!");
        self.mask_image.write().unwrap().mask_not();
        Ok(Response::new(StringResponse {
            message: "Inverted".to_string(),
        }))
    }

    async fn cut_depth(
        &self,
        request: Request<CutDepthRequest>,
    ) -> Result<Response<StringResponse>, Status> {
        println!("Received cut_depth!");
        let inner = request.into_inner();
        let mut depth_image = DepthImage::default();
        depth_image.image = self.mask_image.read().unwrap().image.clone();
        if depth_image
            .load_depth(self.depth.read().unwrap().clone())
            .is_err()
        {
            return Err(Status::new(tonic::Code::Internal, "Failed to apply depth"));
        }
        match inner.cut_type {
            0 => {
                let from = Some(inner.cut_from.max(0).min(255) as u8);
                let to = Some(inner.cut_to.max(0).min(255) as u8);
                let mask = depth_image.slice(from, to);
                *self.mask_image.write().unwrap() = mask;
                Ok(Response::new(StringResponse {
                    message: "Applied mask from depth".to_string(),
                }))
            }
            1 => {
                let (from, to) = depth_image.depth_split(2)[1];
                let mask = depth_image.slice(from, to);
                *self.mask_image.write().unwrap() = mask;
                Ok(Response::new(StringResponse {
                    message: "Applied mask from depth".to_string(),
                }))
            }
            2 => {
                let (from, to) = depth_image.depth_split(2)[0];
                let mask = depth_image.slice(from, to);
                *self.mask_image.write().unwrap() = mask;
                Ok(Response::new(StringResponse {
                    message: "Applied mask from depth".to_string(),
                }))
            }
            3 => {
                let (from, to) = depth_image.depth_split(3)[2];
                let mask = depth_image.slice(from, to);
                *self.mask_image.write().unwrap() = mask;
                Ok(Response::new(StringResponse {
                    message: "Applied mask from depth".to_string(),
                }))
            }
            4 => {
                let (from, to) = depth_image.depth_split(3)[1];
                let mask = depth_image.slice(from, to);
                *self.mask_image.write().unwrap() = mask;
                Ok(Response::new(StringResponse {
                    message: "Applied mask from depth".to_string(),
                }))
            }
            5 => {
                let (from, to) = depth_image.depth_split(3)[0];
                let mask = depth_image.slice(from, to);
                *self.mask_image.write().unwrap() = mask;
                Ok(Response::new(StringResponse {
                    message: "Applied mask from depth".to_string(),
                }))
            }
            _ => Err(Status::new(
                tonic::Code::InvalidArgument,
                "Unknown cut type",
            )),
        }
    }

    type ImageModStream = Self::LoadImageStream;

    async fn image_mod(
        &self,
        request: Request<ImageModRequest>,
    ) -> Result<Response<Self::LoadImageStream>, Status> {
        let req_inner = request.into_inner();
        let preview = req_inner.preview;
        let brightness = req_inner.brightness;
        let contrast = req_inner.contrast;
        let sharpness = req_inner.sharpness;
        println!("Got modify image request. Preview : {}, brightness : {}, contrast : {}, sharpness : {}", preview, brightness, contrast, sharpness);
        let (tx, rx) = mpsc::channel(4);
        let mut img_to_mod = self.mask_image.read().unwrap().clone();
        if brightness != 0 {
            img_to_mod.image_brightness(brightness);
        }
        if contrast != 0 {
            img_to_mod.image_contrast(contrast);
        }
        if sharpness != 0 {
            if sharpness > 0 {
                img_to_mod.image_sharpness(sharpness);
            } else {
                img_to_mod.image_blur(-sharpness);
            }
        }
        let img = image::DynamicImage::ImageRgba8(img_to_mod.image.clone());
        if !preview {
            self.mask_image.write().unwrap().image = img_to_mod.image;
        }
        tokio::spawn(async move {
            let mut bytes: Vec<u8> = Vec::new();
            img.write_to(&mut Cursor::new(&mut bytes), image::ImageFormat::Jpeg)
                .unwrap();
            for chunk in bytes.chunks(4194299) {
                let resp = Ok(ImageResponse {
                    raw_data: chunk.to_vec(),
                });
                tx.send(resp).await.unwrap();
            }
            println!("Modified image was sent");
        });
        Ok(Response::new(Box::pin(
            tokio_stream::wrappers::ReceiverStream::new(rx),
        )))
    }
    async fn save_image(
        &self,
        request: Request<ImageSaveRequest>,
    ) -> Result<Response<StringResponse>, Status> {
        let req_inner = request.into_inner();
        let path = req_inner.path;
        let by_mask = req_inner.by_mask;
        println!(
            "Received save image request, path = {}, by mask = {}",
            path, by_mask
        );
        let mut img_to_save = self.mask_image.read().unwrap().clone();
        if by_mask {
            img_to_save.apply_mask();
        }
        img_to_save.save(path.as_str());
        Ok(Response::new(StringResponse {
            message: "Saved".to_string(),
        }))
    }

    async fn save_mask(
        &self,
        request: Request<ImageSaveRequest>,
    ) -> Result<Response<StringResponse>, Status> {
        let req_inner = request.into_inner();
        let path = req_inner.path;
        let by_mask = req_inner.by_mask;
        println!(
            "Received save mask request, path = {}, by mask = {}",
            path, by_mask
        );
        let img_to_save = self.mask_image.read().unwrap().mask().clone();
        img_to_save.save(path.as_str()).unwrap();
        Ok(Response::new(StringResponse {
            message: "Saved".to_string(),
        }))
    }

    async fn save_depth(
        &self,
        request: Request<ImageSaveRequest>,
    ) -> Result<Response<StringResponse>, Status> {
        let req_inner = request.into_inner();
        let path = req_inner.path;
        let by_mask = req_inner.by_mask;
        println!(
            "Received save depth request, path = {}, by mask = {}",
            path, by_mask
        );
        let img_to_save = self.depth.read().unwrap().clone();
        img_to_save.save(path.as_str()).unwrap();
        Ok(Response::new(StringResponse {
            message: "Saved".to_string(),
        }))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let port = match std::env::var("STEPTH_SERVER_PORT") {
        Ok(p) => p,
        Err(_) => "12321".to_string(),
    };
    let addr = format!("0.0.0.0:{}", port).parse().unwrap();
    let service = StepthServerInstance::default();
    println!("Stepth Server listening on {}", &addr);

    Server::builder()
        .accept_http1(true)
        .add_service(StepthServiceServer::new(service))
        .serve(addr)
        .await?;

    Ok(())
}
