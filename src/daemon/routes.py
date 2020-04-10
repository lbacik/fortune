
from flask import Flask


class Routes():

    app: Flask

    def __init__(self, app: Flask):
        self.app = app

    @app.route("/")
    def main():
        fortune_str = fortune.get_from_file('../../data/test-fortunes')
        return jsonify({'fortune': fortune_str})
