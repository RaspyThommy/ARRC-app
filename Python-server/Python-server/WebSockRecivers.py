from websock import WebSocketServer
from threading import Thread
#import RPi.GPIO as GPIO
#import Motors

class WebSockReciver(Thread):
    def __init__(self, name, address, port):
        Thread.__init__(self)
        self.name = name
        self.address = address
        self.port = port
        self.ready = False
        #self.motor = Motors.motor(15, 14, 17, 18, 27, 22)

    def run(self):
        def on_data_receive(client, data):
            msg = str(data)
            msgType = msg.split(":")[0]
            if(msgType == "Macro"):
                msgSplit = msg.split(":")[1]
                if(msgSplit.split("/")[0] == "Stop"):
                    print("Stop")
                else:
                    count = int(msgSplit.split("/")[0])
                    for n in range(1, count + 1):
                        msgCommand = msgSplit.split("/")[n]
                        if(msgCommand == "Forward"):
                            print(msgCommand)
                            #self.motor.forward(35, 1)
                        elif (msgCommand == "Back"):
                            print(msgCommand)
                            # self.motor.back(35, 1)
                        elif (msgCommand == "Left"):
                            print(msgCommand)
                            # self.motor.left(45, 1)
                        elif (msgCommand == "Right"):
                            print(msgCommand)
                            # self.motor.right(45, 1)
            elif(msgType == "Controler"):
                msgSplit = msg.split(":")[1]
                if(msgSplit == "Forward"):
                    print(msgSplit)
                    #self.motor.forward(50, 1)
                elif(msgSplit == "Back"):
                    print(msgSplit)
                    #self.motor.back(50, 1)
                elif(msgSplit == "Right"):
                    print(msgSplit)
                    #self.motor.right(50, 1)
                elif(msgSplit == "Left"):
                    print(msgSplit)
                    #self.motor.left(50, 1)
            elif(msgType == "Manager"):
                msgSplit = msg.split(":")[1]
                self.conn.close()

        def on_connection_open(client):
            print("Connessione avviata")

        def on_error(exception):
            print("Errore: " + str(exception))

        def on_connection_close(client):
            print("Connessione chiusa")

        def on_server_destruct():
            print("Chiusura del server")
            pass

        print("Creating reciver server")
        serverReciver = WebSocketServer(
            self.address,
            self.port,
            on_data_receive = on_data_receive,
            on_connection_open = on_connection_open,
            on_error = on_error,
            on_connection_close = on_connection_close
        )

        serverReciver.serve_forever()
