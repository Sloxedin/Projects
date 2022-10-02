from flask import Flask
from waitress import serve


app = Flask(__name__)


@app.route("/api/v1/hello-world-10")
def hello_world():
    return "Hello World 10"


if __name__ == '__main__':
    print("Server started")
    serve(app)
