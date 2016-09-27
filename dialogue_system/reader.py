# -*- coding: utf-8 -*-
import csv
from collections import namedtuple


def read_file(file_path='../dialogue_system/dialogue.csv'):
    RuleRecord = namedtuple('RuleRecord', 'type, label, description, text, if_, learn, goto, acc, mode')
    f = open(file_path, 'r')
    f.readline()  # skip description line
    rules = [rule for rule in map(RuleRecord._make, csv.reader(f))]

    return rules

"""
class Manager(object):
    
    def __init__(self):
        self.__rules = read_file()

    def return_goto(self, text):
        rule = self.match_text(text)
        return rule.goto

    def match_text(self, text):
        for rule in self.__rules:
            if rule.type != 'input':
                continue
            if rule.text == text:
                return rule

    def welcome(self):
        for rule in self.__rules:
            if rule.type != 'output start':
                continue
            return rule.goto


class LanguageGenerator(object):

    def __init__(self):
        self.__rules = read_file()

    def return_text(self, goto):
        rule = self.match_goto(goto)
        
        return rule.text

    def match_goto(self, goto):
        for rule in self.__rules:
            if rule.type != 'output' and rule.type != 'output start':
                continue
            if rule.label == goto:
                return rule

        return None


manager = Manager()
language_generator = LanguageGenerator()
goto = manager.welcome()
text = language_generator.return_text(goto)
print('S: {}'.format(text))

while True:
    user_utt = input('U: ')
    goto = manager.return_goto(user_utt)
    text = language_generator.return_text(goto)
    print('S: {}'.format(text))
"""