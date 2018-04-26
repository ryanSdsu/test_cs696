"""
Exercise 11 - sklearn and pickle

For this exercise you will be writing a class for several different generator functions.

1) Write a definition called "forest_predictor". This definition should:
    - accept one mandatory string argument, a string corresponding to the file path of the CSV file to be read
    - accept one mandatory integer argument, the column containing the classification values (0 based),
            this column should be removed from your training data and stored in its own list
    - accept **kwargs for the cases:
        - header = bool   -> if True: remove the first row after reading the CSV file
        - save = string   -> check if a file with the name exists, if so, load it with pickle and do not train
            a new classifier, if the file does not exist, train a classifier and save it to this location with pickle
        - test = 2d list  -> predict the classifications of this test data set and print the resulting list
    - always return the classifier object
    - check for **kwargs using kwargs.get() and default to False or None!
        EX: header_exists = kwargs.get('header', False)
        NOT: header_exists = kwargs['header']  # crashes if header was not specified
"""
import pickle
from sklearn.ensemble import RandomForestClassifier
import os

def forest_predictor(file_path, classifications, **kwargs):
    with open(file_path, 'r') as infile:
        data = [line.replace('\n', '').split(',') for line in infile]

        header_exists = kwargs.get('header', False)
        save_exists = kwargs.get('save', False)
        test_exists = kwargs.get('test', False)

        if header_exists:
            data = data[1:]

        classificationColumn = [line[classifications] for line in data]
        data = [line[:classifications] for line in data]

        clf = RandomForestClassifier(n_estimators=500)
        clf = clf.fit(data, classificationColumn)

        if save_exists in os.listdir("saves"):
            with open(save_exists, 'rb') as infile:
                clf = pickle.load(infile)
        else:
            with open(save_exists, 'wb') as outfile:
                pickle.dump(clf, outfile)

        return clf


if __name__ == '__main__':
    #This example uses the training and testing data from lecture_11, a 'large_dataset.csv' is also available, but not required
    x = [[15,0], [18,60000], [80,30000]]
    clf = forest_predictor('/Users/RJ/PycharmProjects/test_cs696/Exercises/simple_data.csv', 2, header=True, save='saves/random_forest.p', test=x)
    # should print ['0', '1', '1'] and return the classifier so that feature_importances_ can be printed
    print(clf.feature_importances_)