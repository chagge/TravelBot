# -*- coding: utf-8 -*-
import re

from dialogue_system.knowledge.reader import read_locations
from dialogue_system.language_understanding.utils.utils import kansuji2arabic


class RuleBasedAttributeExtractor(object):

    def __init__(self):
        self.__places = read_locations()

    def extract(self, text):
        attribute = {'PLACE': self.__extract_place(text), 'SCHEDULE': self.__extract_schedule(text)}

        return attribute

    def __extract_place(self, text):
        locations = [loc for loc in self.__places if loc in text]
        locations.sort(key=len, reverse=True)
        location = locations[0] if len(locations) > 0 else ''

        return location

    def __extract_schedule(self, text):
        pattern = r'\d月|[一二三四五六七八九十]+月'
        match_obj = re.findall(pattern, text)
        month_str = match_obj[0][:-1] if len(match_obj) > 0 else ''
        month_int = kansuji2arabic(month_str)

        return month_int