# -*- coding: utf-8 -*-
from dialogue_system.bot import Bot
import time


if __name__ == '__main__':
    bot = Bot()

    print('S: こんにちは!')
    print('S: わたくし舞子があなたの旅行先さがしをお手伝いさせていただきます。')
    print('S: 時期はいつ頃とかありますか？')
    while True:
        sent = input('U: ')
        if sent == 'ありがとう':
            print('S: どういたしまして')
            break

        reply = bot.reply(sent)
        print('S: {0}'.format(reply))
