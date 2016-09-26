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
        self.assertTrue(attribute['SCHEDULE'] == '9')
        attribute = self.extractor.extract(text='草津のあたり')
        self.assertTrue(attribute['PLACE'] == '草津')
