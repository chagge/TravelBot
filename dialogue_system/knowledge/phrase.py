# -*- coding: utf-8 -*-
import re
import random
from collections import defaultdict
from .reader import read_dialogues


class PhraseReplacer(object):
    """
    self._phrases = {'possible_action': {'texts': ['旅行先さがしをお手伝いできます。'], 'mode': 'random'},
                     'hello': {'texts': ['こんにちは', '今日は'], 'mode': 'random'}}
    """
    
    def __init__(self):
        self._pattern = re.compile(r'\(\(.*?\)\)')
        self._phrases = self._build_phrases()
        #import pprint
        #pprint.pprint(self._phrases)

    def _build_phrases(self):
        """
        スラッシュ(/)区切りの読み込みは可能。
        複数行の読み込みはまだだめ。
        """
        phrases = defaultdict(dict)
        rules = read_dialogues()
        last_label = ''
        for rule in rules:
            if rule.type not in ['phrase', '']:
                continue
            label, text, mode = rule.label, rule.text, rule.mode
            if rule.type == '':
                label = last_label
                phrases[label]['texts'].append(text)
            else:
                last_label = label
                phrases[label]['texts'] = text.split('/')
            phrases[label]['mode'] = mode or 'random'
            
        return phrases
            
    def replace(self, text):
        match_objs = re.findall(self._pattern, text)
        for match_obj in match_objs:
            phrase = match_obj.strip('()')
            if phrase not in self._phrases:
                continue
            replace_mode = self._phrases[phrase]['mode']
            replaced_texts = self._phrases[phrase]['texts']
            if replace_mode == 'random':
                replaced_text = random.choice(replaced_texts)
            else:
                replaced_text = replaced_texts[0]
            text = text.replace(match_obj, replaced_text)

        return text

    
"""
text = "((hello))。((possible_action))時期はいつ頃とかありますか？"
phrase_replacer = PhraseReplacer()
print(phrase_replacer.replace(text))

text = "((evening))。((possible_action))時期はいつ頃とかありますか？"
print(phrase_replacer.replace(text))

text = "時期はいつ頃とかありますか？"
print(phrase_replacer.replace(text))

text = "((nekoneko))時期はいつ頃とかありますか？"
print(phrase_replacer.replace(text))

text = "(())時期はいつ頃とかありますか？"
print(phrase_replacer.replace(text))
"""