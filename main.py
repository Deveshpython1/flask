from flask import Flask, send_file,jsonify

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_file():
    return jsonify({"name":"devesh pandey bhaiya"})

