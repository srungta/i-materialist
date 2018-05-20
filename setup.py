#!/usr/bin/env python

import os
import json

from six.moves.urllib.request import urlretrieve
from pprint import pprint
import pandas as pd

from materialist.commonconstants import *

def create_folder(FOLDER):
    os.makedirs(FOLDER)

    
def create_image_pickle(JSONFILENAME, OUTPUTFILENAME):
    with open(JSONFILENAME) as data_file:
        data = json.load(data_file)
    images = data['images']
    dataset = {}
    for image in images:
        imageId = image['imageId']
        dataset[imageId] = image
    data = list(dataset.values())
    panda = pd.DataFrame(data)
    print(panda.head())
    panda.to_pickle(OUTPUTFILENAME)

def create_label_pickle(JSONFILENAME, OUTPUTFILENAME):
    with open(JSONFILENAME) as data_file:
        data = json.load(data_file)
    dataset = []
    annotations = data['annotations']
    for annotation in annotations:
        labels = list(annotation['labelId'])
        for label in labels:
            a = {}
            a['imageId'] = annotation['imageId']
            a['labelId'] = label
            dataset.append(a)
    panda = pd.DataFrame(dataset)
    print(panda.head())
    panda.to_pickle(OUTPUTFILENAME)


def main():
    if os.path.isfile(TEST_PICKLE) == False:
        create_image_pickle(TEST_FILE, TEST_PICKLE)
    if os.path.isfile(VALIDATION_PICKLE) == False:
        create_image_pickle(VALIDATION_FILE, VALIDATION_PICKLE)
    if os.path.isfile(TRAIN_PICKLE) == False:
        create_image_pickle(TRAIN_FILE, TRAIN_PICKLE)
        
    if os.path.isfile(VALIDATION_LABEL_PICKLE) == False:
        create_label_pickle(VALIDATION_FILE, VALIDATION_LABEL_PICKLE)
    if os.path.isfile(TRAIN_LABEL_PICKLE) == False:
        create_label_pickle(TRAIN_FILE, TRAIN_LABEL_PICKLE)

if __name__ == '__main__':
    main()
