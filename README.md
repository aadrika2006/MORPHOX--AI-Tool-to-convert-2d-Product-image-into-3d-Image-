# MORPHIX – AI 2D to 3D Product Generator

MORPHIX is an AI-powered system that converts 2D product images into 3D models using computer vision and depth estimation techniques.

Built as a 6th Semester IT PBL Project.

---

## 🚀 Project Overview

MORPHIX takes a 2D image (like shoes, products, objects) and performs:

1. Product Segmentation
2. Depth Estimation
3. 3D Mesh Generation
4. Returns a 3D model file (.obj)

The goal is to automate 3D model generation for e-commerce and AR/VR applications.

---

## 🏗️ Project Architecture

Frontend (React / Static)
↓
FastAPI Backend
↓
Segmentation (SAM)
↓
Depth Estimation (MiDaS)
↓
Mesh Generation (Open3D)
↓
3D Model (.obj)

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python 3.12
- PyTorch
- OpenCV
- Open3D

### AI Models
- TripoSR
- MiDaS – Intel Intelligent Systems Lab

### Frontend
- React (optional)
- Three.js (for 3D visualization)

---

## 📂 Project Structure

ai-3d-product-generator/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ ├── utils/
│ │ ├── segment.py
│ │ ├── depth.py
│ │ └── mesh.py
│
├── frontend/
│ └── public/
│ └── uploads/
│
└── README.md

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

bash
git clone <your-repo-link>
cd ai-3d-product-generator/backend
Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Backend Server
python -m uvicorn app:app --reload


Server runs at:

http://127.0.0.1:8000


Swagger API Docs:

http://127.0.0.1:8000/docs

📤 How to Use

Open /docs

Click POST /upload/

Upload an image

Execute

Backend returns paths for:

Segmented Image

Depth Map

3D Mesh (.obj)

🧠 How It Works
Step 1 – Segmentation

Uses SAM to isolate the product from the background.

Step 2 – Depth Estimation

MiDaS predicts a depth map from the segmented image.

Step 3 – Mesh Generation

Depth map is converted into a point cloud and then into a 3D mesh using Open3D.

⚡ Performance
With GPU

3–8 seconds per image

CPU Only

20–60 seconds per image

🎯 Applications

E-commerce 3D product previews

AR product visualization

Game asset generation

Rapid prototyping

👨‍💻 Authors

Aadrika Awasthi (6th Sem IT)

Project: MORPHIX

📌 Future Improvements

Real-time WebGL viewer

Cloud deployment

Multi-view reconstruction

Texture mapping enhancement

User authentication system

📜 License

This project is built for academic purposes.
