# Multi-Threading
from PySide6.QtCore import QRunnable, Slot
# Web Server
import os
import sys
from bottle import Bottle, run, static_file

# Class to start this file as thread
class WebServerWorker(QRunnable):
    @Slot()  # QtCore.Slot
    def run(self):
        startWebServer()

# Webserver code
def startWebServer():
    # setup Bottle server at root path web
    serve_path = "web"
    app = Bottle()
    @app.route('/<filename:re:.*>')
    def serve(filename):
        path = os.path.join(serve_path, resolve_path(filename))
        # serve file if it exists, otherwise 404
        if os.path.isfile(path):
            return static_file(resolve_path(filename), root=serve_path)  # serve a file
        else:
            return "404"
    # start Bottle server at http://0.0.0.0:8156
    run(app, host="0.0.0.0", port="8156")

def resolve_path(path):
    if (sys.platform == 'win32'):
        return "\\" + path.replace('/', '\\')
    return path