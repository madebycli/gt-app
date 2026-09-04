# Huawei Watch GT 6 Test App

Minimal Lite Wearable proof of concept for the Huawei Watch GT 6. Build and packaging run in GitHub Actions without a Huawei developer account.

## What the app proves

When it starts, the watch should show `GT6 TEST READY`. Tapping `TAP TEST` changes the message to `TOUCH OK` and increments the counter. This proves installation, launch, rendering and touch input.

## Automatic browser-only build

Every push to `main` triggers **Build GT6 Test App** in GitHub Actions. The workflow uses HarmonyOS 6.0 command-line tools, builds the Lite Wearable app, extracts the native Huawei `0xBE` BIN, signs it with the public OpenHarmony development identity and uploads everything as `gt6-test-build`.

No Huawei Developer account, AppGallery Connect project or Huawei cloud credentials are used.

## Files in the GitHub Actions artifact

- `gt6-test-gadgetbridge.bin`: signed `0xBE` Huawei app, this is the first file to test with Gadgetbridge.
- `gt6-test-unsigned.bin`: identical app before the experimental account-free signature, useful as fallback and diagnostics.
- `gt6-test.hap`: normal HAP output from Hvigor.
- `ARTIFACTS.txt`: detected formats, hashes and signing metadata.

## Test on Pixel 9 + Gadgetbridge

1. Open the latest successful **Build GT6 Test App** run in the GitHub Actions tab.
2. Download the `gt6-test-build` artifact on the Pixel 9 and unzip it.
3. Open `gt6-test-gadgetbridge.bin` with Gadgetbridge while the GT 6 is connected.
4. Confirm the installation in Gadgetbridge.
5. On the watch, open **GT6 Test**.
6. Expected initial text: `GT6 TEST READY`.
7. Tap **TAP TEST**. Expected text: `TOUCH OK`, with `Taps: 1`.

If the retail GT 6 rejects `gt6-test-gadgetbridge.bin`, record the exact Gadgetbridge/watch error. The file is structurally signed in Huawei's `hw signed app` BIN format, but the retail watch may reject the public OpenHarmony development certificate because that trust decision is device firmware policy.
