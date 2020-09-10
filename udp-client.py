import socket
import time


serverName = "149.130.223.123"
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)


for i in range(1,11):
    initialTime = time.time()
    message = "ping " + str(i)

    clientSocket.sendto(message.encode(),(serverName, serverPort))

    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        totalTime = time.time()
        RTT = totalTime - initialTime
        print("Message received!", modifiedMessage)
        print("Total RTT:" + str(RTT) + " seconds")
    except socket.timeout:
        print("Request timed out")

clientSocket.close()
