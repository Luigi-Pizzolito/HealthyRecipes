# Request Parsing
import json

# Handler class
class ReqHandler:
    def __init__(self):
        print("Handler: Started")
        
    # Handle requests from Web UI
    def handleRequest(self, message, client, socketserver):
        print("WebSocket: %s" % message.replace("\n",""))

        try:
            # Parse message json
            msg = json.loads(message)
            # Call method in this class with name in req JSON field
            method = getattr(ReqHandler, msg["req"])
            method(self, msg, client, socketserver)
            print("Handler: OK %s" % msg["req"])
        except:
            print("Handler: Invalid socket req: %s" % msg["req"])
            socketserver.send_message(client, '{"res":null}')
            
    ## Request handlers
    def echo(self, msg, client, socketserver):
        socketserver.send_message(client, '{"res":"echo","msg":"%s"}'%msg["msg"]) #echo
