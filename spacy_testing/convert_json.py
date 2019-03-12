import csv
import json

TRAIN_DATA = []

# ifile  = open('team_project.csv', "r")
with open('team_project.csv', "r") as ifile:
    read = csv.reader(ifile)
    # read = csv.DictReader(ifile, delimiter=" ")
    next(read, None)  # skip the headers
    # print(read)
    # for row in read :
    #     print (row)

    for row in read:  # see exav mple above
        print(row)
        entities = []
        sentence = row[0]  
        text = row[1]  
        start = row[2]  
        end = row[3]  
        label = row[4]  
        entities.append((start, end, label))
        # print(entities)
    TRAIN_DATA.append((sentence, {'entities': entities}))
    # print(TRAIN_DATA)