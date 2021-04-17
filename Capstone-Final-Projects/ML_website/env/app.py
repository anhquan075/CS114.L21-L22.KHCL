from flask import Flask 
from flask import render_template,request , redirect
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = '/home/mmlab/github/CS114.L22.KHCL/Capstone-Final-Projects/ML_website/env/static/img/UPLOAD/'

app= Flask(__name__)
app.secret_key = "123456789"
app.config["IMAGE_UPLOADS"] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST" :
        if request.files:
            image = request.files["image"]
            if allowed_file(image.filename):
                image.save(os.path.join(app.config["IMAGE_UPLOADS"],image.filename))
                flash("Image was saved")
            else:
                flash('No selected file')
            return redirect(request.url)

    return render_template("btrap_base.html")
if __name__== "__main__":
    app.run(debug=True)
