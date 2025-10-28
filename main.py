from flask import Flask, send_file,jsonify

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_file():
    return jsonify({"name":"devesh pandey bhaiya"})
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

