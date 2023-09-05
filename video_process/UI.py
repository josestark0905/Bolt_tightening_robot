import math
import threading
import time
from tkinter import *
import tkinter as tk
import keyboard
import read_video
import server_demo
from PIL import Image, ImageTk
import control


class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground


E = []
L = []


# 格式化成2016-03-20 11:45:39形式
def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def say_hi(content):
    all_message = message.get(1.0, "end")
    if len(all_message.split("\n")) + len(content.split("\n")) >= 37:
        message.delete(1.0, "end")
    message.insert(END, get_time() + "\n")
    message.insert(END, content)
    message.insert(END, '\n-----------------------------------------\n')


def say_video():
    say_hi("Starting the video，please wait...press q to quit")
    say = threading.Thread(target=read_video.video_bolt, args=(R'.\demo1.mp4', True,))
    # say = threading.Thread(target=server_demo.socket_service)
    say.setDaemon(True)
    say.start()
    # say.join()


def say_total():
    say = threading.Thread(target=read_video.video_bolt, args=(R'.\demo2.mp4', True, False))
    say.setDaemon(True)
    say.start()


def change_keyboard():
    k = keyboard.get_keys()
    # print(len(E))
    for i in range(22):
        keyboard.set_value(k[i], E[i].get())
        E[i].delete(0, END)
        E[i].insert(0, keyboard.get_value(k[i]))
    say_hi('Change successful！')


def button_change():
    say = threading.Thread(target=change_keyboard)
    say.setDaemon(True)
    say.start()


def keyboard_reset():
    keyboard.reset()
    k = keyboard.get_keys()
    for i in range(22):
        E[i].delete(0, END)
        E[i].insert(0, keyboard.get_value(k[i]))
    say_hi("Reset successful！")


def button_reset():
    say = threading.Thread(target=keyboard_reset)
    say.setDaemon(True)
    say.start()


if __name__ == '__main__':
    '''hello_control = threading.Thread(target=control.run_control,
                                     args=("192.168.43.153", "192.168.43.227",))
    hello_control.setDaemon(True)
    hello_control.start()'''
    top = 0.02
    window = Tk()
    window.title("VINEBOT")
    window['bg'] = 'white'
    # 设置窗口大小
    width = 1000
    height = 600
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(alignstr)
    window.attributes('-alpha', 0.95)
    # 键位表
    all_key = keyboard.get_keys()
    for i in range(22):
        name = all_key[i]
        if i < 11:
            x = 0.03
            y = 0.17
        else:
            i = i - 11
            x = 0.29
            y = 0.21
        L1 = Label(window, text=name, bg="white", fg="steelblue")
        L1.place(relx=x, rely=0.057 * (i + 1) + top, anchor=W)
        L.append(L1)
        E1 = Entry(window, width=6, font=('黑体', 15), bg="white", fg="steelblue", relief="groove")
        E1.place(relx=x + y, rely=0.057 * (i + 1) + top, anchor=W)
        E1.insert(0, keyboard.get_value(name))
        E.append(E1)
    # button of change keyboard
    change = HoverButton(window, text="CHANGE", width=7, command=button_change, bg="aliceblue",
                         fg="steelblue",
                         font=("Noto Sans CJK KR", 15, "bold"), activeforeground="violetred2",
                         activebackground="mistyrose",
                         relief="flat")
    change.place(relx=0.6, rely=0.06 + top, anchor=W)
    reset = HoverButton(window, text="RESET", width=7, command=button_reset, bg="aliceblue",
                        fg="steelblue",
                        font=("Noto Sans CJK KR", 15, "bold"), activeforeground="violetred2",
                        activebackground="mistyrose",
                        relief="flat")
    reset.place(relx=0.72, rely=0.06 + top, anchor=W)

    photo = Image.open("logo.gif")  # 括号里为需要显示在图形化界面里的图片
    h, w = photo.size
    photo = photo.resize((math.ceil(0.55 * h), math.ceil(0.55 * w)))  # 规定图片大小
    img0 = ImageTk.PhotoImage(photo)
    img1 = Label(image=img0)
    img1.place(relx=0.025, rely=0.8 + top, anchor=W)

    # message box
    # set a frame for the message box
    # message_box = Frame(window, height=350, width=400, highlightbackground='black', highlightthickness=1)
    '''var = StringVar()
    w = Label(message_box, textvariable=var, fg='blue', font=("微软雅黑", 10))
    var.set("This area shows message from the program!")
    w.pack()'''
    message_width = math.ceil(window.winfo_width() * 55 / 60)
    message_height = math.ceil(window.winfo_height() * 28 / 50)
    message = Text(window, width=53, height=35, bg="aliceblue", fg="steelblue")
    # message.pack()
    message.place(relx=0.6, rely=0.518 + top, anchor=W)
    # button of showing the bolt video
    video_button_1 = HoverButton(window, width=7, text="CAMERA", command=say_video, bg="aliceblue",
                                 fg="steelblue",
                                 font=("Noto Sans CJK KR", 15, "bold"), activeforeground="violetred2",
                                 activebackground="mistyrose",
                                 relief="flat")
    video_button_1.place(relx=0.84, rely=0.06 + top, anchor=W)
    # button of showing the total video
    '''video_button_2 = Button(window, width=10, text="video total", command=say_hi)
    video_button_2.place(relx=0.56, rely=0.05, anchor=W)'''
    # 进入消息循环
    window.mainloop()
