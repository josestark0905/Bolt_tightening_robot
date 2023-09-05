import cv2
import os
from image_process import projection

save_path = R'.\images'


def show_remove(img_path, wait, remove_bottom, draw=True):
    if draw:
        projection(img_path)
    img = cv2.imread(img_path, 1)
    img1 = cv2.resize(img, (0, 0), fx=1.2, fy=1.2, interpolation=cv2.INTER_NEAREST)
    cv2.imshow('video_1', img1)
    key = cv2.waitKey(wait)
    if remove_bottom:
        os.remove(img_path)
    return key


def video_bolt(video_path, flag=True, draw=True):
    # UI.say_hi("start video\nopenCV version:" + format(cv2.__version__))
    capture = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
    print("openCV version:", format(cv2.__version__))
    # capture.open(R"C:\Users\Archillesheel\Pictures\Camera Roll\bolt_Trim.mp4")
    use_camera = True
    start = False
    if capture.isOpened():
        start = True
    if start:
        print("open the video")
        # total_frame_number = capture.get(cv2.CAP_PROP_FRAME_COUNT)
        # print("total frame number:", total_frame_number)
        frame_number = 0
        while True:
            ret, frame = capture.read()
            frame_number += 1
            '''if frame_number >= 158:
                draw = False'''
            if ret:
                img_path = os.path.join(save_path, str(frame_number) + ".jpg")
                try:
                    cv2.imwrite(img_path, frame)
                    #############################在这一部分中显示图片
                    if os.path.exists(img_path):
                        key = show_remove(img_path, 1, flag, draw)
                        if key == ord('q'):
                            # UI.say_hi("quit the video")
                            cv2.destroyAllWindows()
                            break
                except:
                    print("I'm OK bro!")
                    continue
                #############################
                '''if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                else:
                    frame_number += 1'''
            else:
                cv2.destroyAllWindows()
                break
    capture.release()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    video_bolt("1")
