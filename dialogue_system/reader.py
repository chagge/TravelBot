# -*- coding: utf-8 -*-
import csv
from collections import namedtuple


def read_file(file_path='../dialogue_system/dialogue.csv'):
    RuleRecord = namedtuple('RuleRecord', 'type, label, description, act_type, text, if_, learn, goto, acc, mode')
    f = open(file_path, 'r')
    f.readline()  # skip header line
    rules = [rule for rule in map(RuleRecord._make, csv.reader(f))]

    return rules
