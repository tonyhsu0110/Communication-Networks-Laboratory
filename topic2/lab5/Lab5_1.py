# -*- coding: utf-8 -*-
import time

import RPi.GPIO as GPIO

import telepot
from telepot.loop import MessageLoop

import Adafruit_DHT

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# LED_1_PIN 
''' start of you code '''
PIN = 11
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, False) 
''' end of you code '''

# Setup DHT11 
''' start of you code '''
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']

''' end of you code '''

# GPIO#, ex: GPIO4 = Pin7
''' start of you code '''
gpio = 4
''' end of you code '''

def action(msg):
    # 解析從 Telegram Bot 收到的訊息，取出 chat_id 和 text
    # msg 為 nested dict 
    # 此處會用到的 function
    #   1. msg['...']
    ''' start of you code '''
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Received: {cmd}'.format(cmd = command))
    ''' end of you code '''

    # 判斷接收到的指令並控制 LED 燈
    # 此處會用到的 function
    #    1. GPIO.output(..., ...)
    #    2. telegram_bot.sendMessage(chat_id, message)
    if 'on' in command:
        ''' start of you code '''
        message = "Turned on the light"
        GPIO.output(PIN, 1)
        telegram_bot.sendMessage(chat_id, message)
        ''' end of you code '''
    
    elif 'off' in command:
        ''' start of you code '''
        message = "Turned off the light"
        GPIO.output(PIN, 0)
        telegram_bot.sendMessage(chat_id, message)
        ''' end of you code '''

    # Get humidity & temperature
    # 此處會用到的 function
    #    1.  Adafruit_DHT.read_retry(...., ....)
    ''' start of you code '''
    humid, temp = Adafruit_DHT.read_retry(sensor, gpio)
    humid = str(humid)
    temp = str(temp)
    #print ("the humidity is", humid)
  
    ''' end of you code '''

    # 判斷接收到的指令並透過 Telegram Bot 回傳溫溼度給使用者
    # 此處會用到的 function
    #    1. telegram_bot.sendMessage(chat_id, message)
    ''' start of you code '''
    if 'humid' in command:
        message = "The current humidity is " + humid + "%"
        telegram_bot.sendMessage(chat_id, message)
    elif 'temp' in command:
        message = "The current temperature is " + temp + "*C"
        telegram_bot.sendMessage(chat_id, message)
    ''' end of you code '''

# 填寫當初設定 Telegram Bot 的 token
''' start of you code '''
telegram_bot = telepot.Bot('6947686178:AAErh2qLTSZ9YtURfwrzTZVGAafRfy3MZQ4')
''' end of you code '''

print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Send the command to turn on or off the light...')

while True:
    time.sleep(3)

# # -*- coding: utf-8 -*-
# import time

# import RPi.GPIO as GPIO

# import telepot
# from telepot.loop import MessageLoop

# import Adafruit_DHT

# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)

# # LED_1_PIN 
# ''' start of you code '''
# PIN =                                     
# GPIO.setup(PIN, GPIO.OUT)
# GPIO.output(PIN, False) 
# ''' end of you code '''

# # Setup DHT11 
# ''' start of you code '''
    
# ''' end of you code '''

# # GPIO#, ex: GPIO4 = Pin7
# ''' start of you code '''
# gpio = 4
# ''' end of you code '''

# def action(msg):
#     # 解析從 Telegram Bot 收到的訊息，取出 chat_id 和 text
#     # msg 為 nested dict 
#     # 此處會用到的 function
#     #   1. msg['...']
#     ''' start of you code '''
#     chat_id = 
#     command = 

#     print('Received: {cmd}'.format(cmd = command))
#     ''' end of you code '''

#     # 判斷接收到的指令並控制 LED 燈
#     # 此處會用到的 function
#     #    1. GPIO.output(..., ...)
#     #    2. telegram_bot.sendMessage(chat_id, message)
#     if 'on' in command:
#         ''' start of you code '''


#         ''' end of you code '''
    
#     elif 'off' in command:
#         ''' start of you code '''


#         ''' end of you code '''

#     # Get humidity & temperature
#     # 此處會用到的 function
#     #    1.  Adafruit_DHT.read_retry(...., ....)
#     ''' start of you code '''
  
        
#     ''' end of you code '''

#     # 判斷接收到的指令並透過 Telegram Bot 回傳溫溼度給使用者
#     # 此處會用到的 function
#     #    1. telegram_bot.sendMessage(chat_id, message)
#     ''' start of you code '''
#     if  in command:
        
  
        
#     ''' end of you code '''

#     ''' start of you code '''
#     elif  in command:

  
        
#     ''' end of you code '''

# # 填寫當初設定 Telegram Bot 的 token
# ''' start of you code '''
# telegram_bot = telepot.Bot('xxxxxxxxxxx')
# ''' end of you code '''

# print(telegram_bot.getMe())

# MessageLoop(telegram_bot, action).run_as_thread()
# print('Send the command to turn on or off the light...')

# while True:
#     time.sleep(3)