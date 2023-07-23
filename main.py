from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def run_flask_app(app):
    app.run(use_reloader=False)

flask_thread = threading.Thread(target=run_flask_app, args=(app,))
flask_thread.start()
