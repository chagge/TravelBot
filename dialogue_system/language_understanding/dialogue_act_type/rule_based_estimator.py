# -*- coding: utf-8 -*-


class RuleBasedDialogueActTypeEstimator(object):

    def __init__(self):
        pass

    def estimate(self, attribute):
        if attribute['PLACE'] != '':
            return 'RespondSmallArea'
        elif attribute['SCHEDULE'] != '':
            return 'RespondSchedule'
        else:
            return 'OTHER'
