import random
import sys
import pygame
from pygame import *
import time
import socket
import threading


def Random_Search(A, k):
    record = {}
    while len(record) < len(A):
        i = random.randint(0, len(A) - 1)
        if A[i] == k:
            return i
        else:
            record[i] = A[i]
    return None


def linear_search(A, k):
    for i in range(len(A)):
        if A[i] == k:
            return i
    return None


def scramble_search(A, k):
    index = np.random.permutation(len(A))
    for i in range(len(A)):
        if A[index[i]] == k:
            return index[i]
    return None


pygame.init()
screen_size = (800, 550)
screen = pygame.display.set_mode(screen_size, RESIZABLE)
background = 0, 0, 0  # black
screen.fill(background)
# background = pygame.image.load('cover.JPG').convert()
pygame.display.set_caption("VINEBOT Command Monitor")
fontsize = 50
fontObject = pygame.font.SysFont("arial.ttf", fontsize)
info = display.Info()
textlist = ['']


def start_server(host, buf_size=1024, port=8080):
    print("Hi! Welcome to server!")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)  # 接收的连接数
    client, address = server.accept()  # 因为设置了接收连接数为1，所以不需要放在循环中接收
    while True:  # 循环收发数据包，长连接
        text_printed = False
        text_rec = client.recv(buf_size)
        if not text_printed:
            print(text_rec.decode())
        text_printed = True


def DisplayText(text):
    all_keys_pressed = 0
    for key_condition in pygame.key.get_pressed():
        if key_condition:
            all_keys_pressed += 1
    create_text = fontObject.render(text, True, (255, 255, 255))
    text_position = int(info.current_w / 3.3), int(info.current_h / 4
                                                   + all_keys_pressed * info.current_h / 10)
    screen.blit(create_text, text_position)


def DeleteText(textlist, command):
    screen.fill(background)
    textlist.remove(command)
    textnum = 0
    for text_remain in textlist:
        create_text = fontObject.render(text_remain, True, (255, 255, 255))
        text_position = int(info.current_w / 3.3), int(info.current_h / 4
                                                       + textnum * info.current_h / 10)
        screen.blit(create_text, text_position)
        textnum += 1


def TextResize(textlist):
    screen.fill(background)
    textnum = 0
    for text_remain in textlist:
        create_text = fontObject.render(text_remain, True, (255, 255, 255))
        text_position = int(info.current_w / 3.3), int(info.current_h / 4
                                                       + textnum * info.current_h / 10)
        screen.blit(create_text, text_position)
        textnum += 1


if __name__ == '__main__':
    while True:
        name = input()
        try:
            print(key.key_code(name))
        except ValueError:
            print("no such key")
            continue
