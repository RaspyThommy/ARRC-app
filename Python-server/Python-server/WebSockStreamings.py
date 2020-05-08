from websock import WebSocketServer
from threading import Thread
import cv2
import base64
import time

class WebSockStreaming(Thread):
    def __init__(self, name, address, port):
        Thread.__init__(self)
        self.name = name
        self.address = address
        self.port = port

    def run(self):
        streaming = True

        def on_data_receive(client, data):
            if data == "Manager:Disconnect":
                serverStreaming.close_client(client)
                cam.release()

            elif data == "Manager:cam/320":
                cam.set(3, 320)
                cam.set(2, 240)

            elif data == "Manager:cam/640":
                cam.set(3, 640)
                cam.set(2, 480)

        def on_connection_open(client):
            print("Connection open")
            time.sleep(2)
            serverStreaming.send(client, "Name:R2D2")

            print("Starting streaming video")

            while streaming:
                ret, img = cam.read()
                ret, buffer = cv2.imencode('.jpg', img)
                my_image = base64.b64encode(buffer)
                serverStreaming.send(client, "Img:" + str(my_image))

        def on_error(exception):
            print("Errore: " + exception)

        def on_connection_close(client):
            print("Connessione chiusa")

        def on_server_destruct():
            print("Chiusura del server")
            pass

        print("Creating streaming server")
        serverStreaming = WebSocketServer(
            self.address,
            self.port,
            on_data_receive = on_data_receive,
            on_connection_open = on_connection_open,
            on_error = on_error,
            on_connection_close = on_connection_close
        )

        cam =cv2.VideoCapture(0)

        serverStreaming.serve_forever()
