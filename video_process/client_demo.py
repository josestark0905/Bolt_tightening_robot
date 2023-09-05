import socket
import os
import struct
import time

import cv2


def client_build(ip, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("begin to connect")
            s.connect((ip, port))
            return s
        except socket.error as msg:
            print("finding")


def send_data(s, img_path):
    try:
        # 定义文件头信息，包含文件名和文件大小
        fhead = struct.pack('128sl', bytes(os.path.basename(img_path).encode('utf-8')),
                            os.stat(img_path).st_size)
        fileinfo_size = len(fhead)
        s.send(struct.pack('i', fileinfo_size))
        s.send(fhead)
        print('client filepath: {0}'.format(img_path))
        fp = open(img_path, 'rb')
        while True:
            data = fp.read(1024)
            if not data:
                print('{0} file send over...'.format(img_path))
                break
            s.send(data)
    except socket.error as msg:
        socket_client()


def socket_client():
    s = client_build('192.168.43.153', 8080)
    # print(msg)
    # sys.exit(1)
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
                    send_data(s, img_path)
                    frame_number += 1
        except socket.error as msg:
            socket_client()
    capture.release()
    # print(s.recv(1024))
    # s.close()
    # break


if __name__ == '__main__':
    socket_client()
