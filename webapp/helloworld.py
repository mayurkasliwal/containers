from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Mayur sample web app container is here "

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=12345)