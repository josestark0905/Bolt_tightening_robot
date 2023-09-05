##Last modified on Nov.26
##Contributed by YDX
##Client
import sys
import pygame
from pygame import *
import time
import socket
import threading
import keyboard


def start_server(host, buf_size=1024, port=80):
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


def DisplayText(fontObject, info, screen, text):
    all_keys_pressed = 0
    for key_condition in pygame.key.get_pressed():
        if key_condition:
            all_keys_pressed += 1
    create_text = fontObject.render(text, True, (255, 255, 255))
    text_position = int(info.current_w / 3.3), int(info.current_h / 4
                                                   + all_keys_pressed * info.current_h / 10)
    screen.blit(create_text, text_position)


def DeleteText(screen, background, fontObject, info, textlist, command):
    screen.fill(background)
    textlist.remove(command)
    textnum = 0
    for text_remain in textlist:
        create_text = fontObject.render(text_remain, True, (255, 255, 255))
        text_position = int(info.current_w / 3.3), int(info.current_h / 4
                                                       + textnum * info.current_h / 10)
        screen.blit(create_text, text_position)
        textnum += 1


def TextResize(screen, background, fontObject, info, textlist):
    screen.fill(background)
    textnum = 0
    for text_remain in textlist:
        create_text = fontObject.render(text_remain, True, (255, 255, 255))
        text_position = int(info.current_w / 3.3), int(info.current_h / 4
                                                       + textnum * info.current_h / 10)
        screen.blit(create_text, text_position)
        textnum += 1


def run_control(host_ip, connected_ip):
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
    # host_ip = '172.20.10.6'
    # host_ip = "10.167.89.232"
    # connected_ip = '169.254.130.0'
    # connected_ip = "10.167.89.232"
    port = 8080
    print("I'm client! Hey bro!")
    server = threading.Thread(target=start_server, args=(host_ip,))
    server.setDaemon(True)
    server.start()
    time.sleep(5)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)  # 在客户端开启心跳维护
    client.connect((connected_ip, port))
    while True:
        # client.send('collision detection'.encode())
        time.sleep(0.01)
        for event in pygame.event.get():  # get()获取事件的返回值
            if event.type == pygame.QUIT:  # 判断事件是否是退出事件，是则退出
                client.send('quit'.encode())  # 停止程序
                pygame.quit()  # 先退出pygame窗口
                sys.exit()  # 再退出pygame程序
            elif event.type == pygame.KEYDOWN:  # 捕获按键操作
                if event.key == keyboard.get_key_value('Driver Moving Left'):  # 按下左按键
                    client.send('left'.encode())
                    textlist.append('Driver Moving Left')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Driver Moving Right'):  # 按下右按键
                    client.send('right'.encode())
                    textlist.append('Driver Moving Right')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Middle Leg Rising'):  # 按下上按键
                    client.send('up'.encode())
                    textlist.append('Middle Leg Rising')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Middle Leg Descending'):  # 按下下按键
                    client.send('down'.encode())
                    textlist.append('Middle Leg Descending')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Side Legs Lifting'):  # 按下空格
                    client.send('space'.encode())
                    textlist.append('Side Legs Lifting')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Side Legs Descending'):  # 按下左或右shift
                    client.send('shift'.encode())
                    textlist.append('Side Legs Descending')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Climbing Up'):  # 按下w
                    client.send('w'.encode())
                    textlist.append('Climbing Up')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Climbing Down'):  # 按下s
                    client.send('s'.encode())
                    textlist.append('Climbing Down')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Turning Left'):  # 按下A
                    client.send('a'.encode())
                    textlist.append('Turning Left')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Turning Right'):  # 按下D
                    client.send('d'.encode())
                    textlist.append('Turning Right')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Driver Working'):  # 按下R
                    client.send('r'.encode())
                    textlist.append('Driver Working')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('All Electromagnets Deactivated'):  # 按下P
                    client.send('p'.encode())
                    textlist.append('All Electromagnets Deactivated')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Front Electromagnet Activated'):  # 按下1
                    client.send('1'.encode())
                    textlist.append('Front Electromagnet Activated')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Middle Electromagnet Activated'):  # 按下2
                    client.send('2'.encode())
                    textlist.append('Middle Electromagnet Activated')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Rear Electromagnet Activated'):  # 按下1
                    client.send('3'.encode())
                    textlist.append('Rear Electromagnet Activated')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Front Electromagnet Deactivated'):  # 按下8
                    client.send('8'.encode())
                    textlist.append('Front Electromagnet Deactivated')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Middle Electromagnet Deactivated'):  # 按下9
                    client.send('9'.encode())
                    textlist.append('Middle Electromagnet Deactivated')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Rear Electromagnet Deactivated'):  # 按下0
                    client.send('0'.encode())
                    textlist.append('Rear Electromagnet Deactivated')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Front Leg Lifting'):  # 按下e
                    client.send('e'.encode())
                    textlist.append('Front Leg Lifting')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Front Leg Descending'):  # 按下q
                    client.send('q'.encode())
                    textlist.append('Front Leg Descending')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Rear Leg Lifting'):  # 按下z
                    client.send('z'.encode())
                    textlist.append('Rear Leg Lifting')
                    DisplayText(fontObject, info, screen, textlist[-1])
                elif event.key == keyboard.get_key_value('Rear Leg Descending'):  # 按下c
                    client.send('c'.encode())
                    textlist.append('Rear Leg Descending')
                    DisplayText(fontObject, info, screen, textlist[-1])
            elif event.type == pygame.KEYUP:
                if event.key == keyboard.get_key_value('Driver Moving Left'):  # 松开左键
                    client.send('xleft'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Driver Moving Left')
                elif event.key == keyboard.get_key_value('Driver Moving Right'):  # 松开右键
                    client.send('xright'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Driver Moving Right')
                elif event.key == keyboard.get_key_value('Middle Leg Rising'):  # 松开上键
                    client.send('xup'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Middle Leg Rising')
                elif event.key == keyboard.get_key_value('Middle Leg Descending'):  # 松开下键
                    client.send('xdown'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Middle Leg Descending')
                elif event.key == keyboard.get_key_value('Side Legs Lifting'):  # 松开空格
                    client.send('xspace'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Side Legs Lifting')
                elif event.key == keyboard.get_key_value('Side Legs Descending'):  # 松开左或右shift
                    client.send('xshift'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Side Legs Descending')
                elif event.key == keyboard.get_key_value('Climbing Up'):  # 松开w
                    client.send('xw'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Climbing Up')
                elif event.key == keyboard.get_key_value('Climbing Down'):  # 松开s
                    client.send('xs'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Climbing Down')
                elif event.key == keyboard.get_key_value('Turning Left'):  # 松开A
                    client.send('xa'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Turning Left')
                elif event.key == keyboard.get_key_value('Turning Right'):  # 松开D
                    client.send('xd'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Turning Right')
                elif event.key == keyboard.get_key_value('Driver Working'):  # 松开R
                    client.send('xr'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Driver Working')
                elif event.key == keyboard.get_key_value('All Electromagnets Deactivated'):  # 松开P
                    # client.send('xp'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'All Electromagnets Deactivated')
                elif event.key == keyboard.get_key_value('Front Electromagnet Activated'):  # 松开1
                    DeleteText(screen, background, fontObject, info, textlist, 'Front Electromagnet Activated')
                elif event.key == keyboard.get_key_value('Middle Electromagnet Activated'):  # 松开2
                    DeleteText(screen, background, fontObject, info, textlist, 'Middle Electromagnet Activated')
                elif event.key == keyboard.get_key_value('Rear Electromagnet Activated'):  # 松开3
                    DeleteText(screen, background, fontObject, info, textlist, 'Rear Electromagnet Activated')
                elif event.key == keyboard.get_key_value('Front Electromagnet Deactivated'):  # 松开8
                    DeleteText(screen, background, fontObject, info, textlist, 'Front Electromagnet Deactivated')
                elif event.key == keyboard.get_key_value('Middle Electromagnet Deactivated'):  # 松开9
                    DeleteText(screen, background, fontObject, info, textlist, 'Middle Electromagnet Deactivated')
                elif event.key == keyboard.get_key_value('Rear Electromagnet Deactivated'):  # 松开0
                    DeleteText(screen, background, fontObject, info, textlist, 'Rear Electromagnet Deactivated')
                elif event.key == keyboard.get_key_value('Front Leg Lifting'):  # 松开e
                    client.send('xe'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Front Leg Lifting')
                elif event.key == keyboard.get_key_value('Front Leg Descending'):  # 松开q
                    client.send('xq'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Front Leg Descending')
                elif event.key == keyboard.get_key_value('Rear Leg Lifting'):  # 松开z
                    client.send('xz'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Rear Leg Lifting')
                elif event.key == keyboard.get_key_value('Rear Leg Descending'):  # 松开c
                    client.send('xq'.encode())
                    DeleteText(screen, background, fontObject, info, textlist, 'Rear Leg Descending')
            if event.type == pygame.VIDEORESIZE:  # 如果窗口大小发生了变化
                screen_size_new = event.size  # 返回当前窗口大小--元组(宽,高)
                screen = pygame.display.set_mode(screen_size_new, RESIZABLE)
                info = display.Info()
                fontsize = min(int(screen_size_new[0] / 800 * 50), int(screen_size_new[1] / 550 * 50))
                fontObject = pygame.font.SysFont("arial.ttf", fontsize)
                TextResize(screen, background, fontObject, info, textlist)
                screen_size = screen_size_new
        pygame.display.update()


if __name__ == '__main__':
    run_control("192.168.43.153", "192.168.43.153")
