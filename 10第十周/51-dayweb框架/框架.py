#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/9


import socket


def handle_request(client):
    buf=client.recv(1024)

    client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
    with open("index.html",'rb') as f:
        data=f.read()
    client.send(data)

def main():
    sock=socket.socket()
    sock.bind(("localhost",8000))
    sock.listen(5)

    while True:
        connection,address= sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == "__main__":
    main()















































