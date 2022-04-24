# this is the backend for an image labering system
import uuid
from pathlib import Path

from flask import Flask, request, jsonify

app = Flask(__name__)

# this endpoint allows the upload of an image which then will be saved in the directory "uploads"
@app.route('/upload', methods=['POST'])
def upload_image():
    # get the image from the request
    image = request.files['image']
    image_id = str(uuid.uuid4())
    image.save(f'uploads/{image_id}.jpg')
    return jsonify({'image_id': image_id})

# this endpoint allows the removal of an image from the directory "uploads"
@app.route('/remove', methods=['POST'])
def remove_image():
    image_id = request.form['image_id']
    image_path = Path(f'uploads/{image_id}.jpg')
    if image_path.exists():
        image_path.unlink()
    return jsonify({'image_id': image_id})


# this endpoint allows the change of an existing image
@app.route('/change', methods=['POST'])
def change_image():
    image_id = request.form['image_id']
    image_path = Path(f'uploads/{image_id}.jpg')
    if image_path.exists():
        image = request.files['image']
        image.save(f'uploads/{image_id}.jpg')
    return jsonify({'image_id': image_id})


# this endpoint returns a specified image
@app.route('/image', methods=['POST'])
def get_image():
    image_id = request.form['image_id']
    image_path = Path(f'uploads/{image_id}.jpg')
    if image_path.exists():
        return jsonify({'image_id': image_id, "image": f"http://localhost:5000/uploads/{image_id}.jpg"})
    else:
        return jsonify({'error': 'image not found'})