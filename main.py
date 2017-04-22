#!/usr/bin/python
# coding=utf-8

import os
import random
import telebot
from bot_token import BOT_TOKEN
from x3xb import X3XB
#import bot_utils


haruki = telebot.TeleBot(BOT_TOKEN)
me = haruki.get_me()

print('Bot Account: ', me)

@haruki.message_handler(commands=['start'])
def send_welcome(message):
    haruki.reply_to(message, 'start')

@haruki.message_handler(func=lambda message: True)
def x3xb(message):
    for index in range(len(X3XB)):
        if (X3XB[index] in message.text):
            haruki.send_message(message.chat.id, X3XB[-index-1])










haruki.polling()
