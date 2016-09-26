# -*- coding: utf-8 -*-
from dialogue_system.bot import Bot
import time


if __name__ == '__main__':
    bot = Bot()

    print('S: こんにちは!')
    time.sleep(2)
    print('S: わたくし舞子があなたの旅行先さがしをお手伝いさせていただきます。')
    time.sleep(2)
    print('S: どの辺りに行ってみたいとかありますか？')
    while True:
        sent = input('U: ')
        if sent == 'ありがとう':
            print('S: どういたしまして')
            break

        reply = bot.reply(sent)
        print('S: {0}'.format(reply))
