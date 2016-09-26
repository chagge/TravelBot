# -*- coding: utf-8 -*-


class DialogueState(object):

    def __init__(self):
        self.__state = {'PLACE': None, 'SCHEDULE': None}

    def update(self, dialogue_act):
        self.__state['PLACE'] = dialogue_act.get('PLACE', self.__state['PLACE'])
        self.__state['SCHEDULE'] = dialogue_act.get('SCHEDULE', self.__state['SCHEDULE'])

    def has(self, name):
        return self.__state.get(name, None) != None

    def get_place(self):
        return self.__state['PLACE']

    def get_schedule(self):
        return self.__state['SCHEDULE']

    def clear(self):
        self.__init__()

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)