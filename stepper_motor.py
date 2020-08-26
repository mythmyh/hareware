import RPi.GPIO as gpio
import time
l1 =5
l2=6
l3=13
l4=19


def set_step(h1, h2, h3, h4):
    gpio.output(l1, h1)
    gpio.output(l2, h2)
    gpio.output(l3, h3)
    gpio.output(l4, h4)


def setup():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(l1, gpio.OUT)
    gpio.setup(l2, gpio.OUT)
    gpio.setup(l3, gpio.OUT)
    gpio.setup(l4, gpio.OUT)


def stop():
    set_step(0, 0, 0, 0)


def forward(delay, steps):
    for i in range(0, steps):
        set_step(1, 0, 0, 0)
        time.sleep(delay)
        set_step(0, 1, 0,0)
        time.sleep(delay)
        set_step(0, 0, 1, 0)
        time.sleep(delay)
        set_step(0, 0, 0, 1)
        time.sleep(delay)


def backward(delay, steps):
    for i in range(0, steps):
        set_step(0, 0, 0, 1)
        time.sleep(delay)
        set_step(0, 0, 1, 0)
        time.sleep(delay)
        set_step(0, 1, 0, 0)
        time.sleep(delay)
        set_step(1, 0, 0, 0)
        time.sleep(delay)


def loop():
    while True:
        backward(0.003, 512)
        stop()
        time.sleep(3)


def destroy():
    gpio.cleanup()

time.sleep(2)
setup()
backward(0.002, 300)
stop()
