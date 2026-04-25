import cv2
import numpy as np
import io
import imghdr
import logging
from flask import request, jsonify, send_file, Blueprint
from werkzeug.utils import secure_filename
from PIL import Image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bp = Blueprint('main', __name__)

# ✅ Home route
@bp.route('/')
def home():
    return "Flask is running ✅"


# ✅ Upload route
@bp.route('/upload', methods=['POST'])
def upload():
    try:
        if 'image' not in request.files:
            logger.error("No image part in request")
            return jsonify({'error': 'No image part'}), 400

        image = request.files['image']

        if image.filename == '':
            logger.error("No file selected")
            return jsonify({'error': 'No file selected'}), 400

        filename = secure_filename(image.filename)

        allowed_extensions = {'png', 'jpg', 'jpeg'}
        if not ('.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions):
            logger.error(f"Invalid extension: {filename}")
            return jsonify({'error': 'Invalid file extension'}), 400

        image_content = image.read()
        image.seek(0)

        if imghdr.what(None, h=image_content) not in allowed_extensions:
            logger.error("Invalid image content")
            return jsonify({'error': 'Invalid image file'}), 400

        try:
            img = Image.open(io.BytesIO(image_content))
            img.verify()
        except Exception as e:
            logger.error(f"Pillow validation failed: {e}")
            return jsonify({'error': 'Invalid image'}), 400

        quality = request.form.get('quality', 50, type=int)

        if quality < 0 or quality > 100:
            logger.error(f"Invalid quality: {quality}")
            return jsonify({'error': 'Quality must be 0-100'}), 400

        # IMPORTANT: use image_content, not image.read() again
        img_array = np.frombuffer(image_content, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)

        if img is None:
            logger.error("OpenCV failed to decode image")
            return jsonify({'error': 'Invalid image'}), 400

        _, buffer = cv2.imencode(
            '.jpg',
            img,
            [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        )

        img_io = io.BytesIO(buffer)

        try:
            processed = Image.open(img_io)
            processed.verify()
        except Exception as e:
            logger.error(f"Processed image invalid: {e}")
            return jsonify({'error': 'Processing failed'}), 400

        img_io.seek(0)

        return send_file(img_io, mimetype='image/jpeg')

    except Exception as e:
        logger.exception("Unexpected error occurred")
        return jsonify({'error': 'Something went wrong'}), 500