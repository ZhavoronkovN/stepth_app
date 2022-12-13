fn main () -> Result<(), Box<dyn std::error::Error>> {
    tonic_build::compile_protos("../stepth-protos/stepth.proto")?;
    Ok(())
  }