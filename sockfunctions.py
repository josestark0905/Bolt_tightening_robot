import socket
import time


def start_server(host, buf_size=1024, port=8080):
    print("Hi! Welcome to server!")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)  # 接收的连接数
    client, address = server.accept()  # 因为设置了接收连接数为1，所以不需要放在循环中接收
    while True:  # 循环收发数据包，长连接
        data = client.recv(buf_size)
        print(data.decode())


def start_client(computer, port=8080):
    print("I'm client! Hey bro!")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)  # 在客户端开启心跳维护
    client.connect((computer, port))
    while True:
        to_be_send = input()
        client.send(to_be_send.encode())
        print('send data')
        time.sleep(1)  # 如果想验证长时间没发数据，SOCKET连接会不会断开，则可以设置时间长一点


if __name__ == '__main__':
    start_server("10.167.89.232")
