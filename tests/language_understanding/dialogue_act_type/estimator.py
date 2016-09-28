# -*- coding: utf-8 -*-
import unittest

from dialogue_system.language_understanding.attribute_extraction.rule_based_extractor import RuleBasedAttributeExtractor
from dialogue_system.language_understanding.dialogue_act_type.rule_based_estimator import RuleBasedDialogueActTypeEstimator


class AttributeExtractorTest(unittest.TestCase):

    def setUp(self):
        self.extractor = RuleBasedAttributeExtractor()
        self.estimator = RuleBasedDialogueActTypeEstimator()

    def tearDown(self):
        pass

    def test_extract(self):
        attribute = self.extractor.extract(text='草津のあたり')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'RespondSmallArea')
        attribute = self.extractor.extract(text='東京観光をしたい')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'RespondMiddleArea')
        attribute = self.extractor.extract(text='関東近郊らへん')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'RespondLargeArea')
        attribute = self.extractor.extract(text='9月の第2土曜日あたり')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'RespondSchedule')
        attribute = self.extractor.extract(text='こんにちは')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'OTHER')