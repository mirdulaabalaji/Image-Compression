# 🖼️ Image Compression Web Application

## 📌 Overview

This project is a **full-stack image compression web application** that allows users to upload images, adjust compression quality, and download optimized images.

It consists of:

* 🔧 A **Flask backend API** for image processing
* 🎨 A **React frontend** for user interaction
* 🔗 Seamless integration via HTTP requests (REST API)

---

## 🚀 Motivation

High-resolution images consume significant storage and bandwidth. This project was built to:

* Reduce image size without major quality loss
* Provide a simple UI for compression control
* Demonstrate full-stack development with API integration

---

## 🧱 Tech Stack

### Backend

* **Flask** – Lightweight Python web framework
* **OpenCV (cv2)** – Image compression engine
* **NumPy** – Image array manipulation
* **Pillow (PIL)** – Image validation
* **Flask-CORS** – Cross-origin communication

### Frontend

* **React.js** – UI development
* **Vite** – Fast frontend build tool
* **HTML/CSS** – Styling and layout


---

## ⚙️ Backend Implementation

### 📁 Structure

```
app/
 ├── __init__.py       → App factory & CORS setup
 ├── routes.py         → API endpoints
 ├── models.py         → Placeholder
 └── forms.py          → Optional form handling

run.py                 → Entry point
requirements.txt       → Dependencies
```

---

### 🔌 API Endpoint

#### `POST /upload`

Handles image compression.

### 📥 Request

* Form-data:

  * `file` → Image file (jpg/png/jpeg)
  * `quality` → Compression level (0–100)

---

### ⚙️ Processing Flow

1. Validate file presence
2. Check file type (`imghdr`)
3. Verify image using Pillow
4. Convert image → NumPy array
5. Compress using OpenCV:

   ```python
   cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, quality])
   ```
6. Return compressed image as response

---

### 📤 Response

* Compressed image file (binary stream)

---

## 🎨 Frontend Implementation

### Key Features

* Image upload interface
* Quality slider (user-controlled compression)
* Preview + download option

---

### ⚙️ Workflow

1. User selects an image
2. Adjusts compression quality
3. Clicks upload
4. Sends request to backend using:

   ```javascript
   fetch("http://localhost:5000/upload", {
       method: "POST",
       body: formData
   })
   ```
5. Receives compressed image
6. Displays/downloads result

---

## 🔗 Backend–Frontend Integration

### CORS Configuration

Backend allows frontend communication:

```python
CORS(app, origins=["http://localhost:5173"])
```

### Data Flow

* Frontend sends `multipart/form-data`
* Backend processes image
* Backend returns binary image
* Frontend converts response → downloadable file

---

## ▶️ How to Run

### 1. Clone Repository

```bash
git clone https://github.com/your-username/image-compression-api.git
cd image-compression-api
```

---

### 2. Backend Setup

```bash
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
python run.py
```

Runs on:

```
http://localhost:5000
```

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Runs on:

```
http://localhost:5173
```

---

## 🧪 Example API Usage

Using curl:

```bash
curl -X POST http://localhost:5000/upload \
  -F "file=@image.jpg" \
  -F "quality=50" \
  --output compressed.jpg
```

---

## 📚 Learnings

* Building REST APIs with Flask and POSTMAN
* Handling file uploads securely
* Image processing using OpenCV
* Integrating React with backend APIs
* Managing CORS issues in full-stack apps

---

## 👨‍💻 Author - Me

Developed as a full-stack project to demonstrate backend API design and frontend integration.

---


