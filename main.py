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

# @app.route("/", methods='POST')
# def encrypt():
    # store values of requested text in local variable
    # store value of requested rot in local variable
    # encrypt text using rotate_string
    # return encrypted string wrapped in <h1> tags rendered in browser

app.run()