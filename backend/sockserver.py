# Multi-Threading
from PySide6.QtCore import QRunnable, Slot

# Class to start this file as thread
class SocketServerWorker(QRunnable):
    @Slot()  # QtCore.Slot
    def run(self):
        startSocketServer()

# SocketServer code
def startSocketServer():
    print("SocketServer started!")