"""Optional: store verified Wikimedia Commons photos locally for offline viewing.
Run: python download_photos.py
"""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError
from app_photo_sources import PHOTO_FILES

DEST=Path(__file__).resolve().parent/'assets'/'photos'
DEST.mkdir(parents=True,exist_ok=True)
for name,url in PHOTO_FILES.items():
    try:
        req=Request(url, headers={'User-Agent':'UAE-Maritime-Education/1.0 (classroom project)'})
        with urlopen(req,timeout=20) as res: data=res.read()
        if len(data)<1000 or not data.startswith(b'\xff\xd8'):
            print('Skipped (invalid JPEG):',name)
            continue
        (DEST/name).write_bytes(data)
        print('Saved',name, len(data),'bytes')
    except (OSError, URLError) as ex:
        print('Could not download',name,ex)
print('Done. If downloads were blocked, the app can still display online photos.')
