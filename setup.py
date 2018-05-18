#!/usr/bin/env python

import os
import json

from six.moves.urllib.request import urlretrieve
from pprint import pprint
import pandas as pd

DATA_FOLDER = './materialist/data'
TEST_FOLDER = './materialist/data/test'
TRAIN_FOLDER = './materialist/data/train'
VALIDATION_FOLDER = './materialist/data/validation'

TEST_FILE = './materialist/data/test.json'
TRAIN_FILE = './materialist/data/train.json'
VALIDATION_FILE = './materialist/data/validation.json'


TEST_PICKLE = './materialist/data/test.pickle'
TRAIN_PICKLE = './materialist/data/train.pickle'
VALIDATION_PICKLE = './materialist/data/validation.pickle'


def create_folder(FOLDER):
    os.makedirs(FOLDER)


def create_pickle(JSONFILENAME, OUTPUTFILENAME, has_labels=False):
    with open(JSONFILENAME) as data_file:
        data = json.load(data_file)
    images = data['images']
    dataset = {}
    for image in images:
        imageId = image['imageId']
        dataset[imageId] = image
    if has_labels:
        annotations = data['annotations']
        for annotation in annotations:
            imageId = annotation['imageId']
            dataset[imageId]['labelId'] = list(annotation['labelId'])
    a = list(dataset.values())
    panda = pd.DataFrame(a)
    print(panda.head())
    panda.to_pickle(OUTPUTFILENAME)


def main():
    if os.path.isfile(TEST_PICKLE) == False:
        create_pickle(TEST_FILE, TEST_PICKLE, False)
    if os.path.isfile(VALIDATION_PICKLE) == False:
        create_pickle(VALIDATION_FILE, VALIDATION_PICKLE, True)
    if os.path.isfile(TRAIN_PICKLE) == False:
        create_pickle(TRAIN_FILE, TRAIN_PICKLE, True)


if __name__ == '__main__':
    main()
