#coding: utf-8-*- 
#Author:lxz-hxy
'''
opencv每隔若干秒拍照并且保存
'''
import time
from cv2 import cv2 as cv2
import socket
import threading
from SocketTest import send_big_file_from_socket
import os
def take_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:

        resize = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_NEAREST)
        cv2.imwrite('01.jpg', resize)
    cap.release()
    cv2.destroyAllWindows()
    file_size = os.stat('01.jpg').st_size
    print(file_size)

    return 0 


if __name__ == '__main__':
    print('Begin to take pictures..........')

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 接受完了就会关闭socket,不会抛出错误
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    serv.bind(("192.168.1.73", 12007))
    serv.listen(5)

    clx, address = serv.accept()
    while True:
        k = clx.recv(12)

        print(k.decode('utf-8') + "==========")
        print(len(k))

        take_photo()
        if True:
            dameon = threading.Thread(target=send_big_file_from_socket, args=('192.168.1.73', 12008, '01.jpg'))
            dameon.start()
        clx.send('hello world'.encode('utf-8'))
        print('Finished !!')
