import csv
import sys
import numpy as np

def prepare_data(infile):
    data =  np.loadtxt(infile, delimiter=',')
    intercept_col = np.ones((data.shape[0], 1))
    data = np.concatenate((intercept_col, data), axis=1)
    data[:, 1] = normalize(data[:, 1])
    data[:, 2] = normalize(data[:, 2])
    return data

def normalize(data):
    std, mean = np.std(data), np.mean(data)
    for row in range(data.shape[0]):
        data[row] = (data[row] - mean) / std
    return data