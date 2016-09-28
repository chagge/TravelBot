# -*- coding: utf-8 -*-
from dialogue_system.knowledge.reader import read_dialogues


class LanguageGenerator(object):
    def __init__(self):
        self.__rules = read_dialogues()

    def generate_sentence(self, goto):
        rule = self.match_goto(goto)

        return rule.text

    def match_goto(self, goto):
        for rule in self.__rules:
            if rule.type != 'output' and rule.type != 'output start':
                continue
            if rule.label == goto:
                return rule

        return None