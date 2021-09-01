import time
import RPi.GPIO as GP

GP.setmode(GP.BOARD)
GP.setwarnings(False)

FWD = 13
BACK = 15
LEFT = 11
RIGHT = 7
STOP = 18

RR, RR_DIR1, RR_DIR2 = 33, 35, 37  # REAR RIGHT
RL, RL_DIR1, RL_DIR2 = 40, 38, 36
FR, FR_DIR1, FR_DIR2 = 32, 24, 26
FL, FL_DIR1, FL_DIR2 = 8, 10, 19

# MOTOR:    #HP: DIR1:HIGH e DIR2:LOW il motore gira portando il veicolo in avanti
GP.setup(RR,GP.OUT)
GP.setup(RR_DIR1,GP.OUT)
GP.setup(RR_DIR2,GP.OUT)

GP.setup(RL,GP.OUT)
GP.setup(RL_DIR1,GP.OUT)
GP.setup(RL_DIR2,GP.OUT)

GP.setup(FR,GP.OUT)
GP.setup(FR_DIR1,GP.OUT)
GP.setup(FR_DIR2,GP.OUT)

GP.setup(FL,GP.OUT)
GP.setup(FL_DIR1,GP.OUT)
GP.setup(FL_DIR2,GP.OUT)

PWM_RR = GP.PWM(RR,100)  # set pwm for each motor
PWM_RL = GP.PWM(RL,50)
PWM_FR = GP.PWM(FR,50)
PWM_FL = GP.PWM(FL,50)

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

    GP.output(FR_DIR1, GP.HIGH)
    GP.output(FR_DIR2, GP.LOW)
    PWM_FR.ChangeDutyCycle(pwm_default)

    GP.output(FL_DIR1, GP.HIGH)
    GP.output(FL_DIR2, GP.LOW)
    PWM_FL.ChangeDutyCycle(pwm_default)

def go_bw():    #velocità predefinita

    GP.output(RR_DIR1, GP.LOW)
    GP.output(RR_DIR2, GP.HIGH)
    PWM_RR.ChangeDutyCycle(50)

    GP.output(RL_DIR1, GP.LOW)
    GP.output(RL_DIR2, GP.HIGH)
    PWM_RL.ChangeDutyCycle(50)

    GP.output(FR_DIR1, GP.LOW)
    GP.output(FR_DIR2, GP.HIGH)
    PWM_FR.ChangeDutyCycle(50)

    GP.output(FL_DIR1, GP.LOW)
    GP.output(FL_DIR2, GP.HIGH)
    PWM_FL.ChangeDutyCycle(50)

def go_right(pwm_default,turn_inc):

    GP.output(RR_DIR1, GP.HIGH)
    GP.output(RR_DIR2, GP.LOW)
    PWM_RR.ChangeDutyCycle(pwm_default)

    GP.output(RL_DIR1, GP.LOW)
    GP.output(RL_DIR2, GP.HIGH)
    PWM_RL.ChangeDutyCycle(pwm_default*turn_inc)

    GP.output(FR_DIR1, GP.HIGH)
    GP.output(FR_DIR2, GP.LOW)
    PWM_FR.ChangeDutyCycle(pwm_default)

    GP.output(FL_DIR1, GP.LOW)
    GP.output(FL_DIR2, GP.HIGH)
    PWM_FL.ChangeDutyCycle(pwm_default*turn_inc)

def go_left(pwm_default,turn_inc):

    GP.output(RR_DIR1, GP.LOW)
    GP.output(RR_DIR2, GP.HIGH)
    PWM_RR.ChangeDutyCycle(pwm_default*turn_inc)

    GP.output(RL_DIR1, GP.HIGH)
    GP.output(RL_DIR2, GP.LOW)
    PWM_RL.ChangeDutyCycle(pwm_default)

    GP.output(FR_DIR1, GP.LOW)
    GP.output(FR_DIR2, GP.HIGH)
    PWM_FR.ChangeDutyCycle(pwm_default*turn_inc)

    GP.output(FL_DIR1, GP.HIGH)
    GP.output(FL_DIR2, GP.LOW)
    PWM_FL.ChangeDutyCycle(pwm_default)


def spin_right():
    PWM_RR.ChangeDutyCycle(0)
    PWM_RL.ChangeDutyCycle(0)
    PWM_FR.ChangeDutyCycle(0)
    PWM_FL.ChangeDutyCycle(0)

    GP.output(RR_DIR1, GP.HIGH)
    GP.output(RR_DIR2, GP.LOW)
    PWM_RR.ChangeDutyCycle(30)

    GP.output(RL_DIR1, GP.LOW)
    GP.output(RL_DIR2, GP.HIGH)
    PWM_RL.ChangeDutyCycle(30)

    GP.output(FR_DIR1, GP.HIGH)
    GP.output(FR_DIR2, GP.LOW)
    PWM_FR.ChangeDutyCycle(30)

    GP.output(FL_DIR1, GP.LOW)
    GP.output(FL_DIR2, GP.HIGH)
    PWM_FL.ChangeDutyCycle(30)
def spin_left():

    PWM_RR.ChangeDutyCycle(0)
    PWM_RL.ChangeDutyCycle(0)
    PWM_FR.ChangeDutyCycle(0)
    PWM_FL.ChangeDutyCycle(0)

    GP.output(RR_DIR1, GP.LOW)
    GP.output(RR_DIR2, GP.HIGH)
    PWM_RR.ChangeDutyCycle(30)

    GP.output(RL_DIR1, GP.HIGH)
    GP.output(RL_DIR2, GP.LOW)
    PWM_RL.ChangeDutyCycle(30)

    GP.output(FR_DIR1, GP.LOW)
    GP.output(FR_DIR2, GP.HIGH)
    PWM_FR.ChangeDutyCycle(30)

    GP.output(FL_DIR1, GP.HIGH)
    GP.output(FL_DIR2, GP.LOW)
    PWM_FL.ChangeDutyCycle(30)


fwd = True
back = True
left = True
right = True
stop = True
pwm_go = 50

PWM_RR.start(0)     # set initial value of pwms
PWM_RL.start(0)
PWM_FR.start(0)
PWM_FL.start(0)

while stop:

    stop = GP.input(STOP)
    fwd = GP.input(FWD)
    back = GP.input(BACK)
    left = GP.input(LEFT)
    right = GP.input(RIGHT)

    go_fw(pwm_go)
    time.sleep(2)
    go_bw()
    time.sleep(2)
    PWM_RR.ChangeDutyCycle(0)

    if not fwd:
        go_fw(pwm_go)
        print("fwd")
    # --------------------------
    if not back:
        go_bw()
        print("back")
    # --------------------------
    if not left:
        go_left(pwm_go,1)
        print("left")
    # --------------------------
    if not right:
        go_right(pwm_go,1)
        print("right")
    # --------------------------
    if not stop:
        go_fw(0)
        print("stop")
    # --------------------------