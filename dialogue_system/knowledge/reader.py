# -*- coding: utf-8 -*-
import os
# import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Todo
# 地名、都道府県、地域を階層化

def read_small_areas():
    # 地名の読み込み
    file_path = os.path.join(BASE_DIR, 'locations.txt')
    with open(file_path, 'rb') as f:
        locations = [loc.decode('utf-8').strip() for loc in f]

    return locations


def read_middle_areas():
    # 都道府県の読み込み
    file_path = os.path.join(BASE_DIR, 'prefecture.txt')
    with open(file_path, 'rb') as f:
        middle_areas = [pref.decode('utf-8').strip() for pref in f]

    return middle_areas


def read_large_areas():
    # 地域の読み込み
    file_path = os.path.join(BASE_DIR, 'region.txt')
    with open(file_path, 'rb') as f:
        large_areas = [region.decode('utf-8').strip() for region in f]

    return large_areas


# def read_genres():
#     file_path = os.path.join(BASE_DIR, 'genre.yaml')
#     with open(file_path, 'rb') as f:
#         genres = yaml.load(f)
#
#     return genres