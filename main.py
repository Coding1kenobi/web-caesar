from flask import Flask
from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method='POST'>
            <label>Rotate By
                <input name="rot" type="text" value="0">
            <textarea name="message" rows="10" cols="30"></textarea>
            <input type="submit">
        </form>
      
    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    message = request.form['message']
    rot = int(request.form['rot'])
    encrypted_message = rotate_string(message, rot)
    return encrypted_message
app.run()