from flask import Flask, render_template, request
import os

app = Flask(__name__)
upload_folder = "uploads"

@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/uploads', methods=["POST"])
def upload_image():
    file = request.files["image"]
    os.makedirs(upload_folder, exist_ok=True)
    file.save(os.path.join(upload_folder, file.filename))
    return "Upload successful."

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0")

