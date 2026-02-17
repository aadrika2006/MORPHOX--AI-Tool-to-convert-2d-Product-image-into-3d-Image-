from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
from utils.segment import segment_image
from utils.depth import estimate_depth
from utils.mesh import depth_to_mesh

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "frontend", "public", "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def read_root():
    return {"message": "MORPHIX backend running successfully"}


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 1️⃣ Segment product
    segmented_path = segment_image(file_path)

    # 2️⃣ Depth estimation
    depth_path = estimate_depth(segmented_path)

    # 3️⃣ Convert depth → 3D mesh
    mesh_path = depth_to_mesh(depth_path)

    return JSONResponse({
        "segmented": os.path.relpath(segmented_path, os.path.join(BASE_DIR, "frontend", "public")),
        "depth": os.path.relpath(depth_path, os.path.join(BASE_DIR, "frontend", "public")),
        "mesh": os.path.relpath(mesh_path, os.path.join(BASE_DIR, "frontend", "public"))
    })
