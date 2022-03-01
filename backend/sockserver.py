# Multi-Threading
from PySide6.QtCore import QRunnable, Slot
# Socket Server
from websocket_server import WebsocketServer

# User request handler code
from backend.requesthandler import ReqHandler

# Class to start this file as thread
class SocketServerWorker(QRunnable):
    @Slot()  # QtCore.Slot
    def run(self):
        startSocketServer()

# SocketServer code
def startSocketServer():
    # setup socket server
    server = WebsocketServer(port = 8157, loglevel=20)

    # Called for every client connecting (after handshake)
    def new_client(client, server):
        print("WebSocket: New client connected")
    # Called when a client sends a message
    def message_received(client, server, message):
        ReqHandler.handleRequest(message, client, server)

    server.set_fn_new_client(new_client)
    server.set_fn_message_received(message_received)

    # start socket server at http://0.0.0.0:8157
    server.run_forever()