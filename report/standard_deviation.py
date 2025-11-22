
from mrjob.job import MRJob
from mrjob.step import MRStep
import math

class StandardDeviation(MRJob):

    def mapper_first(self, key, line):
        # Split the line and extract the values
        a = line.split(',')
        val = float(a[0])
        yield None, val

    def reducer_first(self, _, values):
        arr = list(values)
        n = len(arr)

        # Calculate the mean
        mean = sum(arr) / n

        # Calculate the sum of squared differences
        sum_squared_diff = sum((v - mean) ** 2 for v in arr)

        # Calculate the standard deviation
        std_dev = math.sqrt(sum_squared_diff / n)

        yield None, std_dev

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_first,
                reducer=self.reducer_first
            )
        ]

if __name__ == '__main__':
    StandardDeviation.run()

