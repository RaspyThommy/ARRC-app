import cv2
import websock
import base64
import time
import WebSockStreamings
import WebSockRecivers

if __name__ == "__main__":
    print("Starting servers")
    #with threading
    streamingThreading = WebSockStreamings.WebSockStreaming("webSockStreaming", "192.168.1.200", 1500)
    reciverThreading = WebSockRecivers.WebSockReciver("webSockReciver", "192.168.1.200", 1501)

    streamingThreading.start()
    reciverThreading.start()
