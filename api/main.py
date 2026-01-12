from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
import uuid, os

app = FastAPI()
UPLOAD_DIR="/data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/images", StaticFiles(directory=UPLOAD_DIR), name="images")

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    ext = file.filename.split(".")[-1]
    name = f"{uuid.uuid4()}.{ext}"
    path = os.path.join(UPLOAD_DIR, name)
    
    content = await file.read()
    with open(path, "wb") as f:
        f.write(content)
    
    url = f"/images/{name}"
    
    # Simple check for video extension to return correct HTML tag
    if ext.lower() in ['mp4', 'mov', 'avi', 'webm', 'mkv']:
        html_response = f'<video controls src="{url}" style="max-width:100%"></video>'
    else:
        html_response = f'<img src="{url}">'

    return {"url": url, "html": html_response}
