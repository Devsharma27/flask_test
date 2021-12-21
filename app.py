from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
@app.route('/')
def hello():
    app.logger.error('Processing default request again and again')
    app.logging.info("A Info Logging Message")
    return 'hello world Dev!'
if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
