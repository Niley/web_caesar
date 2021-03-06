from flask import Flask, request
import caesar


app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label>Rotate by:</label>
            <input type="text" name="rot" value="0">
            <textarea name="text">{0}</textarea>
            <button>Submit Query</button>
        </form>  
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    encrypted_text = caesar.rotate_string(text, rot)
    return form.format(encrypted_text)

app.run()