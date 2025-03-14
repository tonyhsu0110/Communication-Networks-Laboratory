# 引進函式庫、設定腳位、設定變數
import RPi.GPIO as GPIO
import time
# 忽略警示訊息
GPIO.setwarnings(False)
v=343
TRIG = 16
E = 18
LED = 12

# print '1'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(E, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)
GPIO.setup(LED, GPIO.OUT)

def measure():
    # 發送一個瞬間訊號
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    # 計時
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(E) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(E) == GPIO.HIGH:
        pulse_end = time.time()

    # 距離為(來回總耗時*音速)/2
    t = pulse_end - pulse_start
    d = t * v
    d = d / 2
    return (d*100)

while (1):
    print measure()
    dis=measure()
    # 距離介在10~20: 閃爍
    if dis > 10 and dis < 20:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.2)
    # 距離<10: 恆亮
    elif dis < 10:
        GPIO.output(LED, GPIO.HIGH)
    # 距離>20: 不亮
    else:
        GPIO.output(LED, GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()