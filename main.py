#!/usr/bin/python
# coding=utf-8

import os
import random
import time
import telebot
from bot_token import HARUKI_BOT_TOKEN
from bot_token import KAZUSA_BOT_TOKEN
from x3xb import X3XB
from sinario import SINARIO
#import bot_utils


haruki = telebot.TeleBot(HARUKI_BOT_TOKEN)
kazusa = telebot.TeleBot(KAZUSA_BOT_TOKEN)
print('Bot Account: ', haruki.get_me())
print('Bot Account: ', kazusa.get_me())


@haruki.message_handler(commands=['start'])
def send_welcome(message):
    haruki.reply_to(message, 'start')

@haruki.message_handler(commands=['help'])
def send_help(message):
    haruki.reply_to(message, '源码在https://github.com/libc0607/Haruki_bot，抄了很多@fython的Bot代码')

@haruki.message_handler(commands=['replay'])
def send_replay(message):
    print('white!')
    white_script = random.choice(SINARIO)
    for sentence in white_script:
        print(sentence)
        time.sleep(sentence[1])
        if (sentence[0] == 'haruki'):
            haruki.send_message(message.chat.id, sentence[2])
        elif (sentence[0] == 'kazusa'):
            kazusa.send_message(message.chat.id, sentence[2])
        # 雪菜嘛 以后会有的


@haruki.message_handler(func=lambda message: True)
def x3xb(message):
    for key in X3XB:
        if (key in message.text):
            haruki.send_message(message.chat.id, X3XB[key])
            kazusa.send_message(message.chat.id, X3XB[key])





haruki.polling()
kazusa.polling()
