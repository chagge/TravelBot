# -*- coding: utf-8 -*-
from dialogue_system.dialogue_management.state import DialogueState
from dialogue_system.backend.apis.docomo_dialogue import DocomoDialogAPI
from dialogue_system.knowledge.reader import read_dialogues


class DialogueManager(object):
    def __init__(self):
        self.__rules = read_dialogues()
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
            if rule.act_type == text:
                return rule

    def welcome(self):
        for rule in self.__rules:
            if rule.type != 'output start':
                continue
            return rule.goto