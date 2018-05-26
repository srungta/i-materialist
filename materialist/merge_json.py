import json
import pandas as pd
TRAIN_FILE = './materialist/data/train.json'

with open(TRAIN_FILE) as data_file:
    train_data = json.load(data_file)
urls = pd.DataFrame(train_data['images'])
labels = pd.DataFrame(train_data['annotations'])
train = pd.merge(urls, labels, on='imageId', how='inner')
train.to_pickle('./train_merged.pickle')
train = train[train['imageId'] <= 100]
train.to_pickle('./train_small.pickle')
print(train.head())
