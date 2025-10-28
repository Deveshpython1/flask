from flask import Flask, send_file,jsonify

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_file():
    return jsonify({"name":"devesh pandey bhaiya"})

if __name__ == '__main__':
    # Accessible on local network
    app.run(host='0.0.0.0', port=1234, debug=True)
