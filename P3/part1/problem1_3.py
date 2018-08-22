import csv
import sys

class perceptron(object):
    def __init__(self, infile, outfile, learn_rate = 1, w1 = 0, w2 = 0, b = 0):
        self.infile = infile
        self.w1 = w1
        self.w2 = w2
        self.b = b
        self.learn_rate = learn_rate
        self.outfile = outfile
    
    def main(self):
        while True:
            lw = self.w1, self.w2, self.b
            example_list = self.get_input()
            for i in example_list:
                result = self.predictor(i)
                if result != int(i[2]):
                    self.train(result, i)
            self.write_output()
            if lw[0] == self.w1 and lw[1] == self.w2 and lw[2] == self.b:
                return self.w1, self.w2, self.b
        
            
    def train(self, result, i):
        self.b = round(self.b + self.learn_rate * (int(i[2]) - result),2)
        self.w1 = round(self.w1 + self.learn_rate * (int(i[2]) - result) * int(i[0]), 2)
        self.w2 = round(self.w2 + self.learn_rate * (int(i[2]) - result) * int(i[1]), 2)

    def predictor(self, example):
        activation = (self.w1 * int(example[0])) + (self.w2 * int(example[1])) + self.b
        return 1 if activation >= 0 else -1

    def write_output(self):
        with open(self.outfile, "a", newline='') as w:
            writer = csv.writer(w)
            text = self.w1, self.w2, self.b
            writer.writerow(text)


    def get_input(self):
        example_list = []
        with open(self.infile, "r") as r:
            reader = csv.reader(r)
            for row in reader:
                example_list.append(row)
        return example_list
        
Object = perceptron(sys.argv[1], sys.argv[2])
Object.main()