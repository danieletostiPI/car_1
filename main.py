import time
import RPi.GPIO as GP

GP.setmode(GP.BOARD)
GP.setwarnings(False)

FWD = 13
BACK = 15
LEFT = 11
RIGHT = 7
STOP = 18

RR, RR_DIR1, RR_DIR2 = 40, 38, 36  # REAR RIGHT
RL, RL_DIR1, RL_DIR2 = 33, 35, 37

FR, FR_DIR1, FR_DIR2 = 29, 23, 21  # DA RIVEDERE
FL, FL_DIR1, FL_DIR2 = 26, 24, 22  # DA RIVEDERE

# MOTOR:    #HP: DIR1:HIGH e DIR2:LOW il motore gira portando il veicolo in avanti
GP.setup(RR, GP.OUT)
GP.setup(RR_DIR1, GP.OUT)
GP.setup(RR_DIR2, GP.OUT)

GP.setup(RL, GP.OUT)
GP.setup(RL_DIR1, GP.OUT)
GP.setup(RL_DIR2, GP.OUT)

GP.setup(FR, GP.OUT)
GP.setup(FR_DIR1, GP.OUT)
GP.setup(FR_DIR2, GP.OUT)

GP.setup(FL, GP.OUT)
GP.setup(FL_DIR1, GP.OUT)
GP.setup(FL_DIR2, GP.OUT)

PWM_RR = GP.PWM(RR, 100)  # set pwm for each motor
PWM_RL = GP.PWM(RL, 100)
PWM_FR = GP.PWM(FR, 100)
PWM_FL = GP.PWM(FL, 100)

GP.setup(FWD, GP.IN, pull_up_down=GP.PUD_UP)
GP.setup(BACK, GP.IN, pull_up_down=GP.PUD_UP)
GP.setup(LEFT, GP.IN, pull_up_down=GP.PUD_UP)
GP.setup(RIGHT, GP.IN, pull_up_down=GP.PUD_UP)

GP.setup(STOP, GP.IN, pull_up_down=GP.PUD_UP)


def go_bw(pwm_default):
    GP.output(RR_DIR1, GP.HIGH)
    GP.output(RR_DIR2, GP.LOW)
    PWM_RR.ChangeDutyCycle(pwm_default)

    GP.output(RL_DIR1, GP.HIGH)
    GP.output(RL_DIR2, GP.LOW)
    PWM_RL.ChangeDutyCycle(pwm_default)

    GP.output(FR_DIR1, GP.LOW)
    GP.output(FR_DIR2, GP.HIGH)
    PWM_FR.ChangeDutyCycle(pwm_default)

    GP.output(FL_DIR1, GP.HIGH)
    GP.output(FL_DIR2, GP.LOW)
    PWM_FL.ChangeDutyCycle(pwm_default)


def go_fw(pwm_default):  # velocità predefinita

    GP.output(RR_DIR1, GP.LOW)
    GP.output(RR_DIR2, GP.HIGH)
    PWM_RR.ChangeDutyCycle(pwm_default)

    GP.output(RL_DIR1, GP.LOW)
    GP.output(RL_DIR2, GP.HIGH)
    PWM_RL.ChangeDutyCycle(pwm_default)

    GP.output(FR_DIR1, GP.HIGH)
    GP.output(FR_DIR2, GP.LOW)
    PWM_FR.ChangeDutyCycle(pwm_default)

    GP.output(FL_DIR1, GP.LOW)
    GP.output(FL_DIR2, GP.HIGH)
    PWM_FL.ChangeDutyCycle(pwm_default)


def go_right(pwm_default, turn_inc):
    GP.output(RR_DIR1, GP.HIGH)
    GP.output(RR_DIR2, GP.LOW)
    PWM_RR.ChangeDutyCycle(pwm_default * turn_inc)

    GP.output(RL_DIR1, GP.LOW)
    GP.output(RL_DIR2, GP.HIGH)
    PWM_RL.ChangeDutyCycle(pwm_default * turn_inc)

    GP.output(FR_DIR1, GP.LOW)
    GP.output(FR_DIR2, GP.HIGH)
    PWM_FR.ChangeDutyCycle(pwm_default * turn_inc)

    GP.output(FL_DIR1, GP.LOW)
    GP.output(FL_DIR2, GP.HIGH)
    PWM_FL.ChangeDutyCycle(pwm_default * turn_inc)


def go_left(pwm_default, turn_inc):
    GP.output(RR_DIR1, GP.LOW)
    GP.output(RR_DIR2, GP.HIGH)
    PWM_RR.ChangeDutyCycle(pwm_default * turn_inc)

    GP.output(RL_DIR1, GP.HIGH)
    GP.output(RL_DIR2, GP.LOW)
    PWM_RL.ChangeDutyCycle(pwm_default * turn_inc)

    GP.output(FR_DIR1, GP.HIGH)
    GP.output(FR_DIR2, GP.LOW)
    PWM_FR.ChangeDutyCycle(pwm_default * turn_inc)

    GP.output(FL_DIR1, GP.HIGH)
    GP.output(FL_DIR2, GP.LOW)
    PWM_FL.ChangeDutyCycle(pwm_default * turn_inc)


fwd = True
back = True
left = True
right = True
stop = True
pwm_go = 80
jumpmw = 99
turn_inc = 1

PWM_RR.start(0)  # set initial value of pwms
PWM_RL.start(0)
PWM_FR.start(0)
PWM_FL.start(0)

from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_option_press(self):
        pwm_go = 90
        return pwm_go

    def on_square_press(self):

        go_fw(jumpmw)  # per farlo partire
        time.sleep(0.05)
        go_fw(pwm_go)
        print("fwd")
    # --------------------------
    def on_circle_press(self):
        go_bw(jumpmw)  # per farlo partire
        time.sleep(0.05)
        go_bw(pwm_go)
        print("back")
    # --------------------------
    def on_triangle_press(self):
        go_right(jumpmw, turn_inc)
        time.sleep(0.05)
        go_right(pwm_go, turn_inc)
        print("right")
    # --------------------------
    def on_x_press(self):
        go_left(jumpmw, turn_inc)
        time.sleep(0.05)
        go_left(pwm_go, turn_inc)
        print("left")
    # --------------------------
    def on_x_release(self):
        PWM_RR.ChangeDutyCycle(0)
        PWM_RL.ChangeDutyCycle(0)
        PWM_FR.ChangeDutyCycle(0)
        PWM_FL.ChangeDutyCycle(0)
    def on_square_release(self):
        PWM_RR.ChangeDutyCycle(0)
        PWM_RL.ChangeDutyCycle(0)
        PWM_FR.ChangeDutyCycle(0)
        PWM_FL.ChangeDutyCycle(0)
    def on_triangle_release(self):
        PWM_RR.ChangeDutyCycle(0)
        PWM_RL.ChangeDutyCycle(0)
        PWM_FR.ChangeDutyCycle(0)
        PWM_FL.ChangeDutyCycle(0)
    def on_circle_release(self):
        PWM_RR.ChangeDutyCycle(0)
        PWM_RL.ChangeDutyCycle(0)
        PWM_FR.ChangeDutyCycle(0)
        PWM_FL.ChangeDutyCycle(0)
    def on_R2_press(self):
        PWM_RR.ChangeDutyCycle(0)
        PWM_RL.ChangeDutyCycle(0)
        PWM_FR.ChangeDutyCycle(0)
        PWM_FL.ChangeDutyCycle(0)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()