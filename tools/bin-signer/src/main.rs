use std::error::Error;
use std::path::PathBuf;

use hapsigner::{
    DevelopmentMaterialBuilder, DevelopmentProfileOptions, HapSigner, InputFormat, SignOptions,
};

fn main() -> Result<(), Box<dyn Error>> {
    let mut args = std::env::args().skip(1);
    let input = PathBuf::from(args.next().expect("missing input BIN path"));
    let output = PathBuf::from(args.next().expect("missing output BIN path"));
    let bundle_name = args.next().expect("missing bundle name");

    let material = DevelopmentMaterialBuilder::new(DevelopmentProfileOptions {
        bundle_name,
        ..Default::default()
    })
    .build()?;

    let signer = HapSigner::new(
        material,
        SignOptions {
            compatible_version: 20,
            code_signing: false,
        },
    );

    signer.sign_application_file(&input, &output, InputFormat::Bin)?;
    println!("signed {} -> {}", input.display(), output.display());
    Ok(())
}
