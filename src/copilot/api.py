# this is the backend for an image labeling system
import os
import uuid

from flask import Flask, request

app = Flask(__name__)

# create the directiry "upload" if it does not exist
if not os.path.exists('upload'):
    os.makedirs('upload')


# this endpoint allows the upload of an image which then will be saved
# in the directory uploads
@app.route('/upload', methods=['POST'])
def upload():
    # get the binary image data from request
    image_data = request.files['image']
    image_id = str(uuid.uuid4())
    image_data.save(os.path.join('upload', image_id))

# this endpoint allows the removal of an image from the database
@app.route('/delete', methods=['POST'])
def delete():
    # get the id of the image to be deleted
    image_id = request.form['image_id']
    # remove the image from the database
    os.remove(os.path.join('upload', image_id))
    # return a success message
    return 'success'


# this endpoint allows the change of an existing image
@app.route('/update', methods=['POST'])
def update():
    # get the id of the image to be updated
    image_id = request.form['image_id']
    # get the new image data
    image_data = request.files['image']
    # remove the old image from the database
    os.remove(os.path.join('upload', image_id))
    # save the new image in the database
    image_data.save(os.path.join('upload', image_id))
    # return a success message
    return 'success'


# this endpoint return a specified image
@app.route('/image', methods=['POST'])
def image():
    # get the id of the image to be returned
    image_id = request.form['image_id']
    # return the image and catch the error if the image does not exist
    try:
        return open(os.path.join('upload', image_id), 'rb').read()
    except FileNotFoundError:
        return 'error'