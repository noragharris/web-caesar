from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>

<html>
    <head>
        <style>
            form {
                background-color:#eee;
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
        <form action="/" method="POST">
            <label>Rotate by: 
                <input type="text" name="rot"></input>
            </label>
            <textarea name="text" rows="10" cols="30"></textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""    

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():

    text = request.form['text']
    rot = int(request.form['rot'])
   
    encrypted_text = rotate_string(text, rot)

    return "<h1>" + encrypted_text + "</h1>"

app.run()