from flask import Flask, request, Response
import os
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    print("Hello hello hello")


    return "Hello World"


@app.route('/with_argument')
def with_argument():
    arg = request.args.get("arg")
    return arg, 200


# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=3000)