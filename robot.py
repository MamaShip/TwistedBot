# -*- coding: utf-8 -*-
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from random import randint
import MySQLdb

#请不要直接使用我代码里的token！每个机器人的token是独立的，你需要为自己的机器人生成新的token
updater = Updater(token='362488155:AAHrtcYCxucyZCHA4gcvJwGTZFfwRSUHjWM')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

#从imageUrls.txt读取图片列表
file = open("/root/bot/pic/imageUrls.txt")
image_list = []
for line in file:
    image_list.append(line.strip('\n'))
n = len(image_list)

#bot_name = '@Twisted_bot'
#global bot
#bot = telegram.Bot(token='362488155:AAHrtcYCxucyZCHA4gcvJwGTZFfwRSUHjWM')

#定义各项命令对应的操作
def start(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text="我是游荡的机器人(๑• . •๑)\n @MamaShip 锐意制作中！\n请使用/help 查看可用命令")
def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)
def cat(bot,update):
    global n
    global image_list
    thisTime = randint(1,n)
    bot.sendPhoto(chat_id=update.message.chat_id, photo=image_list[thisTime-1])
def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="不晓得你在说些啥")

def yo(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text="yo!\nyou find me!")
def test(bot,update):
    print bot
    print type(bot)
    print update
    print type(update)

def help(bot,update):
    text = ('/start - 说实话，我不知道你用这个命令能干啥\n'
            '/yo - 跟我打个招呼吧\n'
            '/cat - 我会从裤裆里掏出一张猫片\n'
            '/help - 就是你在看的这个\n')
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

#为对应命令添加句柄到dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

cat_handler = CommandHandler('cat', cat)
dispatcher.add_handler(cat_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


#try yo
yo_handler = CommandHandler('yo', yo)
dispatcher.add_handler(yo_handler)

test_handler = CommandHandler('test', test)
dispatcher.add_handler(test_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
'''
／future
* ／friend Japari图书馆：可以查询自己是什么样的动物 「哇！好厲～害！你是擅長XX的朋友呢！」
* ／son 可以标记谁是自己的儿子
* ／family 查看自己的家谱
'''

#开始接收数据
updater.start_polling()
#提供结束程序的操作
updater.idle()
