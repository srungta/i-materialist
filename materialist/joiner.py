from commonconstants import RESULTS_FOLDER, FINAL_RESULT
import os
from os import listdir
from os.path import isfile, join
import csv

individual_result_files = [f for f in listdir(
    RESULTS_FOLDER) if isfile(join(RESULTS_FOLDER, f))]

final_results = {}

imageId = 1

for result_file in individual_result_files:
    filename = RESULTS_FOLDER + result_file
    filename_w_ext = os.path.basename(os.path.normpath(filename))
    labelId, _ = os.path.splitext(filename_w_ext)
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            imageId = row[0]
            isLabel = row[1]
            if imageId not in final_results:
                final_results[imageId] = []
            if isLabel == '1':
                final_results[imageId].append(labelId)
    csvFile.close()

for row in final_results:
    final_results[row] = " ".join(final_results[row])

with open(FINAL_RESULT, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["id", "predicted"])
    for key, value in final_results.items():
        writer.writerow([key, value])
