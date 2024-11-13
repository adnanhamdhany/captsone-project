from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return jsonify("Hello World!")

@app.route('/adnan', methods=['POST'])
def adnan():
    data = request.get_json(silent=True)
    informasi = "Nama saya " + data["nama"] + " saya kelas " + data["kelas"]
    return informasi


if __name__ == '__main__':
    app.run()