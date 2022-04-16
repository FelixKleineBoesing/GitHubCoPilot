# this is the backend for an image labeling system
from flask import Flask
from flask import Request

app = Flask(__name__)

# this endpoint allows the upload of an image which then will be saved
# in the directory uploads and the meta information will be saved in the postgres table "images_meta_data
@app.route('/upload', methods=['POST'])
def upload():
    request_data = Request.get_data()

