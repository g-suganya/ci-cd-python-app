from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "v1. \nThis message is coming from gcp CloudBuild"

if __name__ == '__main__':
 app.run(debug=True,host='0.0.0.0',port=5000)
app.run(host='0.0.0.0') 