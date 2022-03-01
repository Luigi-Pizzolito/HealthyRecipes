# Multi-Threading
from PySide6.QtCore import QRunnable, Slot

# Class to start this file as thread
class WebServerWorker(QRunnable):
    @Slot()  # QtCore.Slot
    def run(self):
        startWebServer()

# Webserver code goes here
def startWebServer():
    print("WebServer started!")