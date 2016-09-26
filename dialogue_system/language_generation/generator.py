# -*- coding: utf-8 -*-
import sys


class LanguageGenerator(object):

    def __init__(self):
        pass

    def generate_sentence(self, dialogue_act):
        sent = ''
        if 'PLACE' in dialogue_act:
            sent += '場所は{0}ですね。'.format(dialogue_act['PLACE'])
        if 'SCHEDULE' in dialogue_act:
            sent += '{0}ですね。'.format(dialogue_act['SCHEDULE'])

        sys_act_type = dialogue_act['sys_act_type']
        if sys_act_type == 'RequestPlace':
            sent += 'どの辺りに行ってみたいとかありますか？'
        elif sys_act_type == 'RequestSchedule':
            sent += '時期はいつ頃とかありますか?'
        elif sys_act_type == 'CHAT':
            sent += dialogue_act['utt']
        elif sys_act_type == 'Suggest':
            place = '熱海'
            if place:
                sent += 'では、{0}のあたりはどうでしょうか?'.format(place)
            else:
                sent += '申し訳ありません。条件に一致するお店が見つかりませんでした。'
        else:
            print('Error')
            sys.exit(-1)

        return sent