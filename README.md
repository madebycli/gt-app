# Huawei Watch GT 6 Test App

Minimal Lite Wearable proof of concept for the Huawei Watch GT 6. The project is intentionally designed to build in GitHub Actions without a Huawei developer account.

## What the app does

When it starts, the watch should show `GT6 TEST READY`. Tapping the button changes the message to `TOUCH OK` and increments a counter. This proves that the app launches and receives touch input.

## Build

Every push to `main` triggers **Build GT6 Test App** in GitHub Actions. You can also start it manually from the Actions tab.

The workflow uploads an artifact named `gt6-test-build`. Download and unzip it on the Pixel 9.

The `dist/ARTIFACTS.txt` file explains what was produced:

- `gt6-test-gadgetbridge.bin`: preferred test file when the Huawei Lite Wearable build emits the `0xBE` binary format Gadgetbridge recognizes.
- `gt6-test.hap`: original HAP output from Hvigor.
- `NO_GADGETBRIDGE_BIN.txt`: present only when the build did not expose a `0xBE` application binary. In that case do not assume renaming the HAP to BIN will work.

## Test on the watch

1. Pair the GT 6 with Gadgetbridge on the Pixel 9.
2. Download the latest `gt6-test-build` artifact from GitHub Actions.
3. Read `ARTIFACTS.txt`.
4. If `gt6-test-gadgetbridge.bin` exists, open it with Gadgetbridge and install it.
5. If only `gt6-test.hap` exists, keep it for diagnostics and check the workflow output before trying further packaging.

No Huawei developer account, AppGallery Connect project, or Huawei cloud credentials are used by this repository.
