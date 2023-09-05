# 套接字客户端

import socket
import struct
import json


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))
    while True:
        # 1、先收报头的长度
        header_size = struct.unpack('i', client.recv(4))[0]  # 固定收4字节，然后解包，得到报头的长度

        # 2、接收报头
        header_bytes = client.recv(header_size)

        # 3、解析报头
        header_json = header_bytes.decode('utf-8')
        header_dic = json.loads(header_json)

        total_size = header_dic['total_size']

        # 4、根据报头内的信息，收取真实的数据

        with open(R'.\download\0.jpg', 'wb') as f:
            recv_size = 0
            while recv_size < total_size:
                recv_data = client.recv(1024)
                f.write(recv_data)
                recv_size += len(recv_data)


# client.close()
if __name__ == '__main__':
    start_client()
