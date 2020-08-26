import RPi.GPIO as GPIO
import time
from testing_GPIO_ORIGINAL import ultrasonic_ranging
import math
import socket
from get_file_from_socket import get_files_from_socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("192.168.1.73", 12007))

# ctrl+R 替換
def ultrasonic_range():
    distance = ultrasonic_ranging(26, 20)
    print("1号超声波探测常量为:{}".format(distance))
    distance2 = ultrasonic_ranging(17, 27)
    print("2号超声波探测常量为:{}".format(distance2))

    if abs(distance-distance2) > 3:
        ultrasonic_range()

    def insert_in_text(file='log.txt', str1='nothing'):
        with open(file, 'r+') as f1:
            original = f1.read()
            f1.seek(0)
            f1.write(str1 + "\n")
            f1.write(original)
    
    def setup(tr, ec):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(tr, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(ec, GPIO.IN)

    def checkdist(tr, ec):
        GPIO.output(tr, GPIO.HIGH)
        time.sleep(0.0005)
        GPIO.output(tr, GPIO.LOW)
        while not GPIO.input(ec):
            pass
        t1 = time.time()

        while GPIO.input(ec):
            pass
        t2 = time.time()
        return (t2-t1)*340/2*100

    setup(26, 20)
    setup(17, 27)
    min_distance = min(distance, distance2)
    n = 0
    times = 0
    j = 0
    times_1 = 0
    while 1:
        k1 = checkdist(26, 20)
        k2 = checkdist(17, 27)
        time.sleep(0.5)
        if k1 < min_distance-3 and k2 < min_distance-3:

            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" ultrasonic change"
            print("distance first {}, distance second {} ".format(k1, k2), end='  ')
            print(now, end='\n')
            j += 1
            if j == 3:
                if times_1 == 0:
                    
                    server.send('hello world'.encode('utf-8'))
                    time.sleep(3)
                    get_files_from_socket("192.168.1.73", 12008,now+".jpg")
                    server.recv(12)
                    times_1 = time.time()
                    print(now, end=" zzz \n")
                else:
                    k = time.time()-times_1
                    times_1 = time.time()
                    if k > 30:
                        server.send('hello world'.encode('utf-8'))
                        insert_in_text(str1=now+" the door is opening!")
                        print(now, end='\n')
                        time.sleep(3)
                        get_files_from_socket("192.168.1.73", 12008,now+".jpg")
                        server.recv(12)
                j = 0

            if n == 0:
                n = 1
            else:
                n = 0
        else:
            j = 0
        if times == 3000:
            insert_in_text(str1='he maybe has been  out !')
            print('he maybe has been out !')


ultrasonic_range()
