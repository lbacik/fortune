
from flask import Flask, jsonify
from ..fortune.factory import Factory
from ..cli.arguments import parse


app = Flask(__name__)

args = parse()
fortune = Factory.create(args.config)


@app.route("/", methods=['GET'])
def home() -> str:
    fortune_str = fortune.get()
    # paramater ?raw
    return jsonify({'fortune': fortune_str})


# because we use uwsgi
# app.run(port=5000)
