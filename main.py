
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("Bvin.html")
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=8080))

