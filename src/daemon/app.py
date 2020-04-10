
from flask import Flask, jsonify
from ..fortune.factory import Factory


app = Flask(__name__)
fortune = Factory.create()


@app.route("/")
def home():
    fortune_str = fortune.get_from_file('data/test-fortunes')
    return jsonify({'fortune': fortune_str})


app.run(port=5555)
