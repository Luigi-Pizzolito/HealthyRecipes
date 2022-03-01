
def handleRequest(message, client, socketserver):
    print("Client(%d) said: %s" % (client['id'], message))
    socketserver.send_message(client, message) #echo
