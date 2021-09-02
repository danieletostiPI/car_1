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

# MOTOR:    #HP: DIR1:HIGH e DIR2:LOW il motore gira portando il veicolo in avanti
GP.setup(RR,GP.OUT)
GP.setup(RR_DIR1,GP.OUT)
GP.setup(RR_DIR2,GP.OUT)

GP.setup(RL,GP.OUT)
GP.setup(RL_DIR1,GP.OUT)
GP.setup(RL_DIR2,GP.OUT)

PWM_RR = GP.PWM(RR,100)  # set pwm for each motor
PWM_RL = GP.PWM(RL,100)

GP.setup(FWD, GP.IN, pull_up_down=GP.PUD_UP)
GP.setup(BACK, GP.IN, pull_up_down=GP.PUD_UP)
GP.setup(LEFT, GP.IN, pull_up_down=GP.PUD_UP)
GP.setup(RIGHT, GP.IN, pull_up_down=GP.PUD_UP)

GP.setup(STOP, GP.IN, pull_up_down=GP.PUD_UP)


def go_fw(pwm_default):

    GP.output(RR_DIR1, GP.HIGH)
    GP.output(RR_DIR2, GP.LOW)
    PWM_RR.ChangeDutyCycle(pwm_default)

    GP.output(RL_DIR1, GP.HIGH)
    GP.output(RL_DIR2, GP.LOW)
    PWM_RL.ChangeDutyCycle(pwm_default)

def go_bw():    #velocità predefinita

    GP.output(RR_DIR1, GP.LOW)
    GP.output(RR_DIR2, GP.HIGH)
    PWM_RR.ChangeDutyCycle(50)

    GP.output(RL_DIR1, GP.LOW)
    GP.output(RL_DIR2, GP.HIGH)
    PWM_RL.ChangeDutyCycle(50)

def go_right(pwm_default,turn_inc):

    GP.output(RR_DIR1, GP.HIGH)
    GP.output(RR_DIR2, GP.LOW)
    PWM_RR.ChangeDutyCycle(pwm_default)

    GP.output(RL_DIR1, GP.LOW)
    GP.output(RL_DIR2, GP.HIGH)
    PWM_RL.ChangeDutyCycle(pwm_default*turn_inc)

def go_left(pwm_default,turn_inc):

    GP.output(RR_DIR1, GP.LOW)
    GP.output(RR_DIR2, GP.HIGH)
    PWM_RR.ChangeDutyCycle(pwm_default*turn_inc)

    GP.output(RL_DIR1, GP.HIGH)
    GP.output(RL_DIR2, GP.LOW)
    PWM_RL.ChangeDutyCycle(pwm_default)

fwd = True
back = True
left = True
right = True
stop = True
pwm_go = 50

PWM_RR.start(0)     # set initial value of pwms
PWM_RL.start(0)

while stop:

    stop = GP.input(STOP)
    fwd = GP.input(FWD)
    back = GP.input(BACK)
    left = GP.input(LEFT)
    right = GP.input(RIGHT)

    if not fwd:
        go_fw(pwm_go)
        print("fwd")
    # --------------------------
    if not back:
        go_bw()
        print("back")
    # --------------------------
    if not left:
        go_fw(0)
        print("stop motor")
    # --------------------------
    if not right:
        #go_right(pwm_go,1)
        print("right")
    # --------------------------
    if not stop:
        go_fw(0)
        print("stop")
    # --------------------------

PWM_RR.ChangeDutyCycle(0)
PWM_RL.ChangeDutyCycle(0)