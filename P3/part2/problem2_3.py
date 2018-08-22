import csv
import sys
import numpy as np
import data_prep as dp

class LinearR(object):
    def __init__(self, infile, outfile, learning_rate):
        self.infile = infile
        self.outfile = outfile
        self.lr = learning_rate
        self.w = np.zeros(3)

    def main(self):
        for i in range(100):
            data = dp.prepare_data(self.infile)
            n = data.shape[0]
            for row in data:
                pred = self.predict(row[:3])
                true = row[3]
                self.update_w(pred, true, row, n)
        self.write_output()

    def update_w(self, pred, true, row, n):
        for i in range(len(row) - 1):
            self.w[i] -= self.lr / n * (pred - true) * row[i]

    def predict(self, data_row):
        return np.dot(data_row, self.w)

    def get_r(self):
        data = dp.prepare_data(self.infile)
        error = 0
        n = 0
        for row in data:
            pred = self.predict(row[:3])
            true = row[3]
            error += (pred - true) ** 2
            n += 1
        return 0.5 * error / n

    def write_output(self):
        with open(self.outfile, "a", newline='') as w:
            writer = csv.writer(w)
            #alpha, number_of_iterations, b_0, b_age, and b_weight
            text = self.lr, 100, round(self.w[0], 6), round(self.w[1], 6), round(self.w[2], 6)
            writer.writerow(text)

infile, outfile = sys.argv[1], sys.argv[2]
for i in (0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 1, 5, 10):
        Object = LinearR(infile, outfile, i)
        Object.main()

#"input2.csv", "output2.csv"