from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! - My Name is Nat"

if __name__ == "__main__":
    application.run()
