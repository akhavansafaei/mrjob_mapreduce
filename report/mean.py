
from mrjob.job import MRJob

class Mean(MRJob):

    def mapper(self, _, line):
        # Check if the line is a digit and yield key-value pairs
        if line.isdigit():
            yield "mean", int(line)

    def reducer(self, key, values):
        # Calculate the mean
        total = 0
        count = 0
        for value in values:
            total += value
            count += 1
        mean = total / count if count > 0 else 0
        yield key, mean

if __name__ == '__main__':
    Mean.run()

