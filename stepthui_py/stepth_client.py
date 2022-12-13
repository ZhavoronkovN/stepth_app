# This Python file uses the following encoding: utf-8
import grpc
import stepth_pb2
import stepth_pb2_grpc

class StepthClient:
    def __init__(self, server_address = "0.0.0.0", server_port = 12321):
        self.server_channel = grpc.insecure_channel(f"{server_address}:{server_port}")
        self.server_stub = stepth_pb2_grpc.StepthServiceStub(self.server_channel)

    def check_connected(self):
        try:
            return bool(self.server_stub.Beep(stepth_pb2.EmptyRequest()).message)
        except Exception as e:
            print(f"Failed to call server, error : {e}")
            return False

    def load_image(self, path):
        try:
            data = b''
            for resp in self.server_stub.LoadImage(stepth_pb2.LoadImageRequest(path=path)):
                data += resp.rawData
            return data
        except Exception as e:
            print(f"Failed to load image, error : {e}")
            return None

    def load_image_to_current(self, path):
        try:
            data = b''
            for resp in self.server_stub.LoadImageToCurrent(stepth_pb2.LoadImageRequest(path=path)):
                data += resp.rawData
            return data
        except Exception as e:
            print(f"Failed to load image, error : {e}")
            return None

    def load_depth(self, path):
        try:
            self.server_stub.LoadDepth(stepth_pb2.LoadImageRequest(path=path))
            return True
        except Exception as e:
            print(f"Failed to load depth, error : {e}")
            return False

    def load_depth_from_additional(self, path):
        try:
            self.server_stub.LoadDepthFromAdditional(stepth_pb2.LoadImageRequest(path=path))
            return True
        except Exception as e:
            print(f"Failed to load depth, error : {e}")
            return False

    def show_depth(self, show):
        try:
            data = b''
            for resp in self.server_stub.HighlightDepth(stepth_pb2.HighlightRequest(enabled=show)):
                data += resp.rawData
            return data
        except Exception as e:
            print(f"Failed to show depth, error {e}")
            return None

    def show_mask(self, show):
        try:
            data = b''
            for resp in self.server_stub.HighlightMask(stepth_pb2.HighlightRequest(enabled=show)):
                data += resp.rawData
            return data
        except Exception as e:
            print(f"Failed to mask depth, error {e}")
            return None

    def select_depth(self, type, f = 0, t = 0):
        try:
            self.server_stub.CutDepth(stepth_pb2.CutDepthRequest(cutType=type, cutFrom=f, cutTo=t))
            return True
        except Exception as e:
            print(f"Failed to load depth, error : {e}")
            return False

    def invert_depth(self):
        try:
            self.server_stub.InvertDepth(stepth_pb2.EmptyRequest())
            return True
        except Exception as e:
            print(f"Failed to load depth, error : {e}")
            return False

    def invert_mask(self):
        try:
            self.server_stub.InvertMask(stepth_pb2.EmptyRequest())
            return True
        except Exception as e:
            print(f"Failed to load depth, error : {e}")
            return False

    def modify_image(self, preview, brightness, contrast, sharpness):
        try:
            data = b''
            for resp in self.server_stub.ImageMod(stepth_pb2.ImageModRequest(preview=preview, brightness=brightness, contrast=contrast, sharpness=sharpness)):
                data += resp.rawData
            return data
        except Exception as e:
            print(f"Failed to change brightness, error {e}")
            return None
