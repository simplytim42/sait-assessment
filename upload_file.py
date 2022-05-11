import os
from flask import request

def upload_file(upload_folder):
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(upload_folder, filename))
    return filename