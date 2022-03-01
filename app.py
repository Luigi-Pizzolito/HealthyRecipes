# General
import os
from time import sleep
# Multi-Threading
from PySide6.QtCore import QThreadPool
# UI Window
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineQuick import QtWebEngineQuick

# User server code from backend
from backend.webserver import WebServerWorker
from backend.sockserver import SocketServerWorker


if __name__ == '__main__':
    # Setup GUI
    ## Load embeded web browser UI from QML file
    QtWebEngineQuick.initialize()
    app = QApplication([])
    engine = QQmlApplicationEngine()
    qml_file_path = os.path.join(os.path.dirname(__file__), 'backend/embeddedbrowser.qml')
    qml_url = QUrl.fromLocalFile(os.path.abspath(qml_file_path))
    engine.load(qml_url)

    # Start server threads
    threadpool = QThreadPool()
    print("Multithreading with maximum %d threads" % threadpool.maxThreadCount())
    ## Start web server
    threadpool.start(WebServerWorker())
    ## Start WebSocket server
    threadpool.start(SocketServerWorker())

    # Start GUI Window
    sleep(2)
    print("Starting main app window.")
    app.exec()