import RPi.GPIO as GPIO
import time


def ultrasonic_ranging(tr, ec):

    def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(tr, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(ec, GPIO.IN)

    def get_distance():
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
    
    setup()
    sources = []
    for x in range(1, 30):
        k = int(get_distance())
        sources.append(k)
        time.sleep(0.5)
    k = set(sources)
    k = sorted(k)
    l1 = list(k)
    if len(l1) > 2:
        j = l1[len(l1) - 2:len(l1)]
        return j[0]

    else:
        return l1[0]


if __name__ == "__main__":
    print(ultrasonic_ranging(17, 27))


