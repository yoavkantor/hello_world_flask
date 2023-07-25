import logging
import threading
from time import sleep

def init_logger(suffix=''):
    from logging import getLogger, getLevelName, Formatter, StreamHandler
    log = getLogger()
    log.setLevel(getLevelName('INFO'))
    log_formatter = Formatter("%(asctime)s [%(levelname)s] %(filename)s %(lineno)d: %(message)s [%(threadName)s] " + suffix)

    console_handler = StreamHandler()
    console_handler.setFormatter(log_formatter)
    log.handlers = []
    log.addHandler(console_handler)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


from werkzeug.serving import make_server

class ServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.server = make_server('127.0.0.1', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        logging.info('starting server')
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

#
# def run_flask_app():
#     app.run(use_reloader=False)
#
# def stop_flask_app():
#     from flask import request
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()

class FlaskRunner():
    def start_server(self):
        self.server = ServerThread(app)
        self.server.start()
        logging.info('server started')

    def stop_server(self):
        logging.info('stopping server')
        self.server.shutdown()
        self.server.join()
        logging.info('server stopped')


if __name__ == '__main__':
    init_logger()
    runner = FlaskRunner()
    runner.start_server()
