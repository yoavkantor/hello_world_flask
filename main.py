from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
class FlaskRunner():
    def run_flask(self):
        app.run(use_reloader=False)
