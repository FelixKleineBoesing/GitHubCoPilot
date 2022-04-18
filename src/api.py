# this is the backend for the image labeling service
import os
import uuid

from flask import Flask, request, jsonify

app = Flask(__name__)



# this endpoint allows the upload of an image which will be saved in the directory "uploads"
@app.route('/upload', methods=['POST'])
def upload():
    # get the image from the request
    image = request.files['image']
    image_id = str(uuid.uuid4())
    # save the image
    image.save('uploads/' + image_id)
    # return the image id
    return image_id


# this endpoiint allows the removal of an image
@app.route('/remove', methods=['POST'])
def remove():
    # get the image id from the request
    image_id = request.form['image_id']
    # remove the image
    image = 'uploads/' + image_id
    if image:
        try:
            os.remove(image)
        except OSError:
            pass
    # return the image id
    return image_id


# this endpoint allows the change of an existing image
@app.route('/change', methods=['POST'])
def change():
    # get the image id from the request
    image_id = request.form['image_id']
    # get the new image from the request
    image = request.files['image']
    # save the new image
    image.save('uploads/' + image_id)
    # return the image id
    return image_id


# this endpoint returns a specified image
@app.route('/image', methods=['POST'])
def image():
    # get the image id from the request
    image_id = request.form['image_id']

    # return the image and catch the error if the image does not exist
    try:
        return open('uploads/' + image_id, 'rb').read()
    except FileNotFoundError:
        return jsonify({'error': 'image not found'})