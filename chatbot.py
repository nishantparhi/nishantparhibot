#!/usr/bin/env python # -*- coding: utf-8 -*-
import telebot
import sys
import os
import subprocess

reload(sys)
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot("") #It's something like 123456789:ABCd1eFg2HijklmnOpqrstUvWXyz12A345

@bot.message_handler(commands=['start']) # This will react to the /start command
def send_welcome(message):
    una = message.from_user.first_name
    bot.reply_to(message, "Hello " + str(una)) # This will be the reaction of the bot to the /start command

@bot.message_handler(commands=['about']) # The /about command
def send_welcome(message):
    bot.reply_to(message, "Hi there\nl I am NPbot created by [Nishant Parhi](http://nishantparhi.me/)", disable_web_page_preview="True", parse_mode="Markdown") # The reaction to the /about command

@bot.message_handler(commands=['help']) # This is the /help command
def send_welcome(message):
    bot.reply_to(message, "Why do you need help?") # This is the reaction of the bot to the /help command

@bot.message_handler( func=lambda message: message.text in ['hi', 'Hello', 'Hi', 'hello', 'hola', 'Hola', 'Howdy', 'Hey', 'hey', 'Yo', 'yo']) # This is a example message
def greetings(m):
 cid = m.chat.id
 uid = m.from_user.id
 bot.send_message(cid, "Hey there nice to meet you!!", disable_web_page_preview="True", parse_mode="Markdown") # This is the reaction to the example message

@bot.message_handler( func=lambda message: message.text in ['how are you?', 'How are you?', 'how are you', 'How are you']) # This is a example message
def greetings_reply(m):
 cid = m.chat.id
 uid = m.from_user.id
 bot.send_message(cid, "I am Great!", disable_web_page_preview="True", parse_mode="Markdown")

@bot.message_handler( func=lambda message: message.text in ['What are you up to', 'what are you up to', 'ssup', 'Ssup', 'sup', 'Sup', "What's up", "what's up"]) # This is a example message
def whatsup(m):
 cid = m.chat.id
 uid = m.from_user.id
 bot.send_message(cid, "Nothing Much! Just Learning new stuff!", disable_web_page_preview="True", parse_mode="Markdown")

@bot.message_handler( func=lambda message: message.text in ['mark']) # This is a example message
def test(m):
 cid = m.chat.id
 uid = m.from_user.id
 arch = subprocess.check_output("google nishant parhi | sed -n 1,5p", shell=True);
 bot.send_message(cid, arch, disable_web_page_preview="True", parse_mode="Markdown")
 
@bot.message_handler(func=lambda message: True)
def echo_all(message): # This means that when the user sends a message or command to the bot that it doens't supports it will react with a message
    bot.send_chat_action(message.chat.id, 'typing') # This simple piece of script will let the user know that the bot is typing...
    bot.reply_to(message, "Sorry, I currently don't support that message.", parse_mode="Markdown") # Here you can change the custom unknown message / command message

bot.polling()
