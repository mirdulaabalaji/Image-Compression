\# 🖼️ Image Compression Web App



\## 📌 Overview



This project is a \*\*full-stack image compression web application\*\* that allows users to upload images, compress them by adjusting quality, and download the optimized result.



The system is built using a \*\*Flask backend API\*\* and a \*\*React (Vite) frontend\*\*, connected through REST APIs.



\---



\## 🎯 Motivation



High-resolution images consume significant storage and bandwidth. This project was built to:



\* Reduce image size efficiently

\* Provide a simple UI for users to control compression quality

\* Demonstrate full-stack development and API integration



\---



\## 🧱 Tech Stack



\### 🔹 Backend



\* Python

\* Flask

\* OpenCV (cv2)

\* NumPy

\* Pillow (PIL)

\* Flask-CORS

\* Werkzeug



\### 🔹 Frontend



\* React.js (Vite)

\* Axios (for API calls)

\* HTML/CSS



\---



\## ⚙️ System Architecture



```

\[ React Frontend ]  →  \[ Flask API Server ]  →  \[ Image Processing ]

&#x20;       |                        |                      |

&#x20;  Upload Image           Validate Input        Compress Image

&#x20;  Set Quality  ───────→  Process Request  ───→  Return Output

```



\---



\## 🔌 Backend Implementation



\### 📁 Structure



```

app/

&#x20;├── \_\_init\_\_.py      # App factory \& CORS setup

&#x20;├── routes.py        # API endpoints

&#x20;├── models.py        # Placeholder (not heavily used)

&#x20;├── forms.py         # Optional

&#x20;└── templates/

```



\---



\### 🚀 App Initialization



\* Uses \*\*Flask Application Factory Pattern\*\*

\* Enables CORS to allow frontend communication



```python

CORS(app, origins=\["http://localhost:5173"])

```



\---



\### 📡 API Endpoint



\#### `POST /upload`



Handles image upload and compression.



\---



\### 🔄 API Workflow



1\. \*\*Receive Request\*\*



&#x20;  \* Accepts `multipart/form-data`

&#x20;  \* Fields:



&#x20;    \* `file` → image

&#x20;    \* `quality` → compression level (0–100)



2\. \*\*Validation\*\*



&#x20;  \* Check file existence

&#x20;  \* Validate extension (`jpg`, `jpeg`, `png`)

&#x20;  \* Verify actual image type using:



&#x20;    \* `imghdr`

&#x20;    \* `PIL`



3\. \*\*Processing\*\*



&#x20;  \* Convert image → NumPy array

&#x20;  \* Compress using OpenCV:



&#x20;  ```python

&#x20;  cv2.imencode('.jpg', img, \[cv2.IMWRITE\_JPEG\_QUALITY, quality])

&#x20;  ```



4\. \*\*Response\*\*



&#x20;  \* Returns compressed image as binary response



\---



\## 🎨 Frontend Implementation



\### 📁 Structure



```

src/

&#x20;├── components/

&#x20;├── App.jsx

&#x20;├── main.jsx

```



\---



\### 🖥️ Features



\* Upload image

\* Adjust compression quality (slider/input)

\* Preview compressed image

\* Download result



\---



\### 🔗 API Integration



\* Uses \*\*Axios\*\* to call backend



```javascript

const formData = new FormData();

formData.append("file", image);

formData.append("quality", quality);



const response = await axios.post(

&#x20; "http://localhost:5000/upload",

&#x20; formData,

&#x20; { responseType: "blob" }

);

```



\---



\### 🔄 Frontend Workflow



1\. User selects image

2\. User sets quality

3\. Sends POST request to backend

4\. Receives compressed image (blob)

5\. Displays/downloads output



\---



\## 🔗 Backend ↔ Frontend Integration



\* Backend runs on: `http://localhost:5000`

\* Frontend runs on: `http://localhost:5173`



\### Key Integration Points:



\* CORS enabled in Flask

\* Axios handles HTTP requests

\* Binary image response handled using `blob`



\---



\## 🧪 How to Run Locally



\### 🔹 Backend



```bash

cd backend

python -m venv venv

venv\\Scripts\\activate   # Windows



pip install -r requirements.txt

python run.py

```



\---



\### 🔹 Frontend



```bash

cd frontend

npm install

npm run dev

```



\---



\## 📷 Supported Formats



\* JPG

\* JPEG

\* PNG (converted to JPEG during compression)



\---



\## ⚠️ Limitations



\* PNG transparency is lost

\* No file size restriction

\* No drag-and-drop UI

\* No authentication system



\---



\## 🚀 Future Improvements



\* Add WebP support

\* Preserve PNG transparency

\* Add drag-and-drop UI

\* Deploy using Docker

\* Add cloud storage (AWS S3 / Firebase)



\---



\## 📌 Key Learnings



\* Building REST APIs using Flask

\* Image processing with OpenCV

\* Handling file uploads securely

\* Frontend–backend integration

\* Working with binary data (blob responses)



\---



\## 📜 License



This project is open-source and free to use.



\---



\## 🙌 Acknowledgements



\* Flask Documentation

\* OpenCV Documentation

\* React + Vite ecosystem



