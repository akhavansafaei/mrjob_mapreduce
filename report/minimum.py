
from mrjob.job import MRJob

class Minimum(MRJob):

    def mapper(self, _, line):
        income = float(line.strip())
        yield "min", income

    def reducer(self, key, values):
        min=1e20
        for value in values:
          if value<min:
            min=value
        min_income=min
        # method 2
        #min_income = min(values)
        yield key, min_income

if __name__ == '__main__':
    Minimum.run()
