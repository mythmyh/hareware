import pygame, time

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
    if xboxController.get_init() == True: print("Initialized properly")
    while 1:
        #trial += 1
        #print(trial)
        pygame.event.get()
        for a in range(3, 5):
            if xboxController.get_axis(a) != 0.0:
                num_axes=xboxController.get_axis(a)
                print('num_axes {} value{}'.format(a, num_axes))
        for b in range(0, xboxController.get_numballs()):
            if xboxController.get_ball(b) != 0:
                ball_nums = xboxController.get_ball(b)
                print("xbox ball {} value {}".format(b, ball_nums))
        for c in range(0, xboxController.get_numbuttons()):
            if xboxController.get_button(c) != 0:
                k=xboxController.get_button(c)
                print("xbox button {} value{}".format(c, k))

        for d in range(0, xboxController.get_numhats()):
            if xboxController.get_hat(d) != (0, 0):
                hat_num=xboxController.get_hat(d)
                print("hat {} value{}".format(d, hat_num))
except KeyboardInterrupt:
    pygame.joystick.quit()
    quit()
