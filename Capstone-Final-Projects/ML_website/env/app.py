from flask import Flask 
from flask import render_template,request , redirect
import os

app= Flask(__name__)

app.config["IMAGE_UPLOADS"] = r"C:\ML_website\env\static\img\UPLOAD"

@app.route('/',methods=["GET","POST"])
def index():

    if request.method == "POST" :
        if request.files:
                image = request.files["image"]

                image.save(os.path.join(app.config["IMAGE_UPLOADS"],image.filename))

                print("Image was saved")
                return redirect(request.url)

    return render_template("btrap_base.html")
if __name__== "__main__":
    app.run(debug=True)
