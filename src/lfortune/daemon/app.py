
from flask import Flask, jsonify

from ..cli.cli import get_config_values
from ..fortune.config import Config
from ..fortune.factory import Factory
from ..cli.arguments import parse


app = Flask(__name__)

args = parse()
config = Config(args.config)
config_values = get_config_values(args, config)

fortune = Factory.create(config_values)


@app.route("/", methods=['GET'])
def home() -> str:
    fortune_str = fortune.get()
    return jsonify({'fortune': fortune_str})

# commented out because of uwsgi
# app.run(port=5000)
