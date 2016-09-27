# -*- coding: utf-8 -*-
from dialogue_system.dialogue_management.state import DialogueState
from dialogue_system.backend.apis.docomo_dialogue import DocomoDialogAPI
from dialogue_system.reader import read_file


class DialogueManager(object):
    def __init__(self):
        self.__rules = read_file()
        self.dialogue_state = DialogueState()

    def update_dialogue_state(self, dialogue_act):
        self.dialogue_state.update(dialogue_act)

    def select_action(self, text):
        act_type = text['user_act_type']
        rule = self.match_text(act_type)
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