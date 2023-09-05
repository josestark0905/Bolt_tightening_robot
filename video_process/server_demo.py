import socket
import threading
import sys
import os
import struct
import datetime
import cv2
import math


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('192.168.43.153', 8080))  # 这里换上自己的ip和端口
        s.listen(10)
        print("Waiting...")
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    conn, addr = s.accept()
    deal_data(conn, addr)
    '''while True:
        conn, addr = s.accept()
        deal_data(conn, addr)
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()'''


def deal_data(conn, addr):
    print('Accept new connection from {0}'.format(addr))
    while True:
        fileinfo_size = struct.calcsize('128sl')
        buf = conn.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sl', buf)
            fn = filename.strip(str.encode('\00'))
            new_filename = os.path.join(str.encode('.\\download\\'),
                                        str.encode(datetime.datetime.now().strftime('%S%f')) + str.encode("0.jpeg"))
            print('file new name is {0}, filesize is {1}'.format(new_filename, filesize))
            recvd_size = 0  # 定义已接收文件的大小
            try:
                fp = open(new_filename, 'wb')
                print("start receiving...")
                while recvd_size < filesize:
                    data = conn.recv(1024)
                    recvd_size += len(data)
                    fp.write(data)
                '''while not recvd_size >= filesize:
                    if filesize - recvd_size > 1024:
                        data = conn.recv(1024)
                        recvd_size += len(data)
                    else:
                        data = conn.recv(filesize - recvd_size)
                        recvd_size = filesize'''
                fp.close()
                print("end receive...")
                name = new_filename.decode()
                os.remove(name)
                print("remove")
                '''name = new_filename.decode()
                img = cv2.imread(name, 1)
                cv2.imshow("video", img)
                print("remove")
                key = cv2.waitKey(1)
                os.remove(name)
                if key == ord('q'):
                    cv2.destroyAllWindows()
                    break'''
            except UnicodeDecodeError:
                continue
            except struct.error:
                continue
            except ValueError:
                continue
            except cv2.error:
                continue

            # cv2.waitKey(1)
    conn.close()
    # break


if __name__ == '__main__':
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    socket_service()
