# encoding: utf-8

from flask import Flask
from flask import request
from main import getSource, postData

app = Flask(__name__)


@app.route("/", methods=['GET'])
def root_get():
    print("Accessing data..")

    try:
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        distance = request.args.get('distance')

        result = getSource(latitude, longitude, distance)
        return result

    except Exception as e:
        return print(e)


@app.route("/", methods=['POST'])
def root_post():
    print("Sending data..")

    try:
        return postData(request.json)

    except Exception as e:
        return print(e)


if __name__ == "__main__":
    app.run()
