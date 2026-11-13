# Open Pearls of the Past on a phone

## Easiest: mobile-friendly web app (no app store)

1. Upload `app.py`, `requirements.txt`, `.streamlit/config.toml`, and the `assets` folder to a GitHub repository. Add `app_photo_sources.py` and optional `download_photos.py`, `PHOTO_CREDITS.md` as well.
2. Visit https://share.streamlit.io, log in with GitHub, select **Create app**, select your repository and the `app.py` file, then deploy.
3. Open the HTTPS `*.streamlit.app` link on a phone (this is public only if you configure it as public).
4. Android: Open link in Chrome → ⋮ → **Add to Home screen**. Some devices show **Install app**. iPhone: open in Safari → Share → **Add to Home Screen**.
5. Tap the icon; app still needs internet access to run because Streamlit code executes on a server.

The icon/name may show Streamlit rather than your custom branding, depending on the browser and Streamlit host. This is a phone-friendly website shortcut, **not a native APK/IPA**.

## A real native mobile app

Rebuild the interface in Flutter or React Native, connect to a Python API for game/data logic, package and test for Android/iOS, then follow app-store requirements. Streamlit itself does not export APK/IPA. A separate Progressive Web App wrapper can provide a custom installable icon but requires extra frontend hosting.

## When testing with students

Use a school-approved hosting/sharing process. No student names or identifiable photos are required. The example score currently exists only in the user's active session and is not a permanent class leaderboard.
