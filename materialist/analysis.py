from commonconstants import *
import pandas as pd
import matplotlib.pyplot as plt

def read_dataset(filename):
    return pd.read_pickle(filename)

# train = read_dataset(TRAIN_PICKLE)
# validation = read_dataset(VALIDATION_PICKLE)
# train_labels = read_dataset(TRAIN_LABEL_PICKLE)
validation_labels = read_dataset('./data/validation_label.pickle')

validation_labels.groupby('imageId')['labelId'].count().plot(kind="bar")
plt.show()
print("DOne")