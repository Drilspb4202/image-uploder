from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
import uuid, os

app = FastAPI()
UPLOAD_DIR="/data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/images", StaticFiles(directory=UPLOAD_DIR), name="images")

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    ext=file.filename.split(".")[-1]
    name=f"{uuid.uuid4()}.{ext}"
    path=os.path.join(UPLOAD_DIR,name)
    with open(path,"wb") as f:
        f.write(await file.read())
    url=f"/images/{name}"
    return {"url":url,"html":f'<img src="{url}">'}
