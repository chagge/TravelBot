# -*- coding: utf-8 -*-
from dialogue_system.reader import read_file


class LanguageGenerator(object):
    def __init__(self):
        self.__rules = read_file()

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