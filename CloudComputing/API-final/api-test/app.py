from flask import Flask, jsonify
from data import get_random_fish
from data2 import get_random_freshness
app = Flask(__name__)

@app.route('/scan', methods=['GET'])
def APItest():

    fish = get_random_fish()
    freshness = get_random_freshness()

    response_text = f"Hasil Scan: \nJenis Ikan - {fish['Jenis Ikan']}, \nTingkat Kesegaran - {freshness['Tingkat Kesegaran']}"

    return response_text

if __name__ == '__main__':
    app.run()
