# 引入模組、設定腳位和GPIO
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

GPIO.setwarnings(False)

TRIG = 16
E = 18
LED = 12

# print '1'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(E, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)
GPIO.setup(LED, GPIO.OUT)

# 設定DHT11
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
sensor = sensor_args['11']
# GPIO第四腳位
dht_pin = 4

def measure(v):
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(E) == 0:
        pulse_start = time.time()
    while GPIO.input(E) == 1:
        pulse_end = time.time()

    t = pulse_end - pulse_start
    d = t * v
    d = d / 2
    return d * 100

while 1:
    H, T = Adafruit_DHT.read_retry(sensor, dht_pin)
    # 音速公式
    v = 331 + 0.6 * T
    # 印出溫度和速度
    print ("==========================")
    print ("Temp:" + str(T) + "*C")
    print ("V=331+0.6*" + str(T))
    print ("="+str(v))
    # 計算距離並print
    d = measure(v)
    print ("Distance : " + str(d))
    # 判斷距離並決定LED燈行為
    if d > 10 and d < 20:
        GPIO.output(LED, 1)
        time.sleep(0.2)
        GPIO.output(LED, 0)
        time.sleep(0.2)
        GPIO.output(LED, 1)
        time.sleep(0.2)
        GPIO.output(LED, 0)
        time.sleep(0.2)
        GPIO.output(LED, 1)
        time.sleep(0.2)
        GPIO.output(LED, 0)
    elif d < 10:
        GPIO.output(LED, 1)
    else:
        GPIO.output(LED, 0)
    time.sleep(0.2)
GPIO.cleanup()