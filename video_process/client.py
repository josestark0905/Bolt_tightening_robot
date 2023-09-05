# 套接字服务端

import cv2
import socket
import struct
import json
import os
import sys


def socket_service():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 8080))
        server.listen(5)
        print("Waiting...")
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    capture = cv2.VideoCapture(0)
    print("openCV version:", format(cv2.__version__))
    # capture.open(video_path)
    use_video = False
    start = False
    if capture.isOpened() or use_video:
        start = True
    if start:
        print("open the video")
        # total_frame_number = capture.get(cv2.CAP_PROP_FRAME_COUNT)
        # print("total frame number:", total_frame_number)
        frame_number = 0
        try:
            while True:
                if frame_number == 100:
                    frame_number = 0
                ret, frame = capture.read()
                if ret:
                    img_path = os.path.join(R'.\images', str(frame_number) + ".jpeg")
                    cv2.imwrite(img_path, frame)
                    send_data(server, img_path)
                    frame_number += 1
        except socket.error as msg:
            socket_service()
    capture.release()


def send_data(conn, file):
    # 1、制作报头
    header_dic = {
        'total_size': os.path.getsize(file),
        'md5': '123svsaef123sdfasdf',
        'filename': os.path.basename(file)
    }
    header_json = json.dumps(header_dic)
    header_bytes = header_json.encode('utf-8')

    # 2、先发送报头的长度
    header_size = len(header_bytes)
    conn.send(struct.pack('i', header_size))  # 把一个整型数字打包成固定字节数(i模式为4字节)的字节对象

    # 3、发送报头
    conn.send(header_bytes)

    # 4、发送真实的数据
    with open(file, 'rb') as fp:
        while True:
            data = fp.read(1024)
            if not data:
                print('{0} file send over...'.format(file))
                break
            conn.send(data)


if __name__ == '__main__':
    socket_service()
'''conn.close()
server.close()'''
