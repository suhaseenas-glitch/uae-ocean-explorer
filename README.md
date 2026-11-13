# Pearls of the Past, Oceans of the Future — Mobile-friendly edition

## Changes
- High-contrast, readable **light** app theme with navy text and teal buttons.
- Responsive mobile-friendly Streamlit layout.
- **Real** photos of a traditional dhow, pearl oysters, and sea turtle from Wikimedia Commons with photo credits.
- Original activities preserved: UAE heritage, NASA research, quiz, pearl-diving simulation, dhow captain, ocean rescue, achievements.
- Photos require internet on first use; optionally run `python download_photos.py` to save local copies. See `PHOTO_CREDITS.md`.

## Windows instructions
1. Extract ZIP.
2. Open the extracted folder containing `app.py`.
3. Type `cmd` in File Explorer address bar.
4. Run:

    python -m pip install -r requirements.txt
    python -m streamlit run app.py

5. Browser opens at `http://localhost:8501`. After installing requirements once, you can also double-click `START_ON_WINDOWS.bat`.

If you are offline, original vector illustrations are stored in `assets/` as optional manual replacements and licensed photo URLs may be unavailable; use `download_photos.py` while online for local photos.

## Mobile app instructions
See `MOBILE_GUIDE.md` for deploying on Streamlit Community Cloud and adding to Android/iOS home screens. Streamlit is a mobile-friendly **web app**, not an Android APK or iOS IPA.

## Scientific and cultural accuracy
The pearl-diving, dhow and ocean rescue games use fictional score values. The NASA research section requires students to bring their own genuine NASA Worldview observations; the photographic images are not NASA data. For the 2026 NASA Space Apps challenge, the submitted project should align with the **official challenge brief** and meaningfully analyze actual NASA observations, not just provide a heritage quiz.
