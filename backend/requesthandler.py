# Request Parsing
import json

# Handler class
class ReqHandler:
        
    # Handle requests from Web UI
    def handleRequest(message, client, socketserver):
        print("WebSocket: %s" % message.replace("\n",""))

        try:
            # Parse message json
            msg = json.loads(message)
            # Call method in this class with name in req JSON field
            method = getattr(ReqHandler, msg["req"])
            method(msg, client, socketserver)
            print("ReqHandler: OK %s" % msg["req"])
        except:
            print("ReqHandler: Invalid socket req: %s" % msg["req"])
            socketserver.send_message(client, '{"res":null}')
            

            
    ## Request handlers
    def echo(msg, client, socketserver):
        socketserver.send_message(client, '{"res":"echo","msg":"%s"}'%msg["msg"]) #echo
