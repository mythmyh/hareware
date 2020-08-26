import pygame, time
from stepper_motor import backward,stop,forward,setup
pygame.init()
pygame.joystick.init()

try:
    xboxController = pygame.joystick.Joystick(0)
    xboxController.init()
    print(xboxController.get_name())
    print("Axes", (xboxController.get_numaxes()))
    print("Balls", xboxController.get_numballs())
    print("Buttons", xboxController.get_numbuttons())
    print("Hats", xboxController.get_numhats())
    times = []
    ultra_skills = []
    ultra_skills_os = [(0, 1), (1, 0), (-1, 0), (0, -1), 0, 1]

    if xboxController.get_init():
        print("Initialized properly")
    while 1:
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.JOYBUTTONUP:
                print('hello world {} joy button up'.format(event.button))
            elif event.type == pygame.JOYBUTTONDOWN:
                print('hello world {} joy button down'.format(event.button))
                ultra_skills.append(event.button)
                print(ultra_skills)

                if ultra_skills == ultra_skills_os:
                    ultra_skills.clear()
                    setup()
                    forward(0.003, 512)
                    stop()

            elif event.type == pygame.JOYHATMOTION:
                print("hello world {} joy button down {}".format(event.hat, event.value))
                if event.value == (0, 1):
                    ultra_skills.clear()
                if event.value != (0, 0):
                    ultra_skills.append(event.value)

            elif event.type == pygame.JOYAXISMOTION:
                print(event.value)

        for a in range(3, 5):
            if xboxController.get_axis(a) != 0.0:
                print(xboxController.get_axis(a))
                print('helloworld')
                backward(0.002, 1)
                stop()
                print(a)
        for b in range(0, xboxController.get_numballs()):
            if xboxController.get_ball(b) != 0:
                print(xboxController.get_ball(b))
        for c in range(0, xboxController.get_numbuttons()):
            if xboxController.get_button(c) != 0:
                k = xboxController.get_button(c)
                #print("xbox button {} value{}".format(c, k))

        for d in range(0, xboxController.get_numhats()):
            if xboxController.get_hat(d) != (0, 0):
                kv = xboxController.get_hat(d)
                times.append(kv)
                #print("lengths is {}".format(len(times)))


except KeyboardInterrupt:
    pygame.joystick.quit()
    quit()
