from PIL import Image
from PIL import ImageDraw as process
import math


def projection(img_path):
    im = Image.open(img_path)
    w, h = im.size
    # print(w, h)
    drawer = process.Draw(im)
    center = (math.ceil(263*w/600), math.ceil(533*h/1000))
    length = math.ceil(w/40)
    length1 = math.ceil(w/88)
    drawer.ellipse((center[0] - length, center[1] - length, center[0] + length, center[1] + length), width=6,
                   outline='blue')
    drawer.line((center[0] - length1, center[1], center[0] + length1, center[1]), fill="green", width=5)
    drawer.line((center[0], center[1] + length1, center[0], center[1] - length1), fill="green", width=5)
    '''point_1 = (center[0] + math.ceil(length / 2), center[1] + math.ceil(length * math.sqrt(3) / 2))
    point_2 = (center[0] - math.ceil(length / 2), center[1] + math.ceil(length * math.sqrt(3) / 2))
    point_3 = (center[0] - length, center[1])
    point_4 = (center[0] - math.ceil(length / 2), center[1] - math.ceil(length * math.sqrt(3) / 2))
    point_5 = (center[0] + math.ceil(length / 2), center[1] - math.ceil(length * math.sqrt(3) / 2))
    point_6 = (center[0] + length, center[1])
    drawer.line((point_1[0], point_1[1], point_2[0], point_2[1]), fill="green", width=6)
    drawer.line((point_2[0], point_2[1], point_3[0], point_3[1]), fill="green", width=6)
    drawer.line((point_3[0], point_3[1], point_4[0], point_4[1]), fill="green", width=6)
    drawer.line((point_4[0], point_4[1], point_5[0], point_5[1]), fill="green", width=6)
    drawer.line((point_5[0], point_5[1], point_6[0], point_6[1]), fill="green", width=6)
    drawer.line((point_6[0], point_6[1], point_1[0], point_1[1]), fill="green", width=6)'''
    im.save(img_path)


R'''if __name__ == '__main__':
    im = Image.open(R'.\images\666.jpg')
    w, h = im.size
    print(w, h)
    drawer = process.Draw(im)
    drawer.line((50, 50, 300, 300), fill="green", width=2)
    im.save(R'.\images\666.jpg')
    # im.show()
    # im.save(R'.\images\red.jpg')'''
