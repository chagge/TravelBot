# -*- coding: utf-8 -*-
from copy import deepcopy

from dialogue_system.dialogue_management.state import DialogueState
from dialogue_system.backend.apis.docomo_dialogue import DocomoDialogAPI


class DialogueManager(object):

    def __init__(self):
        self.dialogue_state = DialogueState()

    def update_dialogue_state(self, dialogue_act):
        self.dialogue_state.update(dialogue_act)

    def select_action(self, dialogue_act):
        sys_act = deepcopy(dialogue_act)
        if dialogue_act['user_act_type'] == 'OTHER':
            api = DocomoDialogAPI()
            reply = api.reply(dialogue_act['utt'])
            sys_act['sys_act_type'] = 'CHAT'
            sys_act['utt'] = reply
        elif not self.dialogue_state.has('PLACE'):
            sys_act['sys_act_type'] = 'RequestPlace'
        elif not self.dialogue_state.has('SCHEDULE'):
            sys_act['sys_act_type'] = 'RequestSchedule'
        else:
            sys_act['sys_act_type'] = 'Suggest'
            sys_act['restaurant'] = 'suggest place'
            self.dialogue_state.clear()

        return sys_act
