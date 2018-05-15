#!/usr/bin/env python

import os
import json

from six.moves.urllib.request import urlretrieve
from pprint import pprint

DATA_FOLDER = './materialist/data'
TEST_FOLDER = './materialist/data/test'
TRAIN_FOLDER = './materialist/data/train'
VALIDATION_FOLDER = './materialist/data/validation'

TEST_FILE = './materialist/data/test.json'
TRAIN_FILE = './materialist/data/train.json'
VALIDATION_FILE = './materialist/data/validation.json'


def create_folder(FOLDER):
    os.makedirs(FOLDER)


def get_images(JSONFILENAME, FOLDER):
    with open(JSONFILENAME) as data_file:
        data = json.load(data_file)
    images = data['images']
    for image in images:
        url = image['url']
        filename = str(image['imageId']) + '.jpg'
        filename = os.path.join(FOLDER, filename)
        if os.path.isfile(filename) == False:
            try:
                f, _ = urlretrieve(url, filename)
                print('Downloaded : ', filename)
            except:
                print('Error downloading : ', filename)
        else:
            print('Found : ', filename)

def main():
    print('Downloading test images')
    if os.path.isdir(TEST_FOLDER) == False:
        create_folder(TEST_FOLDER)
    get_images(TEST_FILE, TEST_FOLDER)

    print('Downloading train images')
    if os.path.isdir(TRAIN_FOLDER) == False:
        create_folder(TRAIN_FOLDER)
    get_images(TRAIN_FILE, TRAIN_FOLDER)

    print('Downloading validation images')
    if os.path.isdir(VALIDATION_FOLDER) == False:
        create_folder(VALIDATION_FOLDER)
    get_images(VALIDATION_FILE, VALIDATION_FOLDER)


if __name__ == '__main__':
    main()
