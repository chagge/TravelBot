# -*- coding: utf-8 -*-
import unittest

from dialogue_system.language_understanding.attribute_extraction.rule_based_extractor import RuleBasedAttributeExtractor


class AttributeExtractorTest(unittest.TestCase):

    def setUp(self):
        self.extractor = RuleBasedAttributeExtractor()

    def tearDown(self):
        pass

    def test_extract(self):
        attribute = self.extractor.extract(text='9月の第2土曜日あたり')
        self.assertTrue(attribute['date'] == '9')
        attribute = self.extractor.extract(text='草津のあたり')
        self.assertTrue(attribute['small_area'] == '草津')
        attribute = self.extractor.extract(text='東京らへん')
        self.assertTrue(attribute['middle_area'] == '東京')
        attribute = self.extractor.extract(text='関東近郊')
        self.assertTrue(attribute['large_area'] == '関東')