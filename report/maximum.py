
from mrjob.job import MRJob

class Maximum(MRJob):

    def mapper(self, _, line):
        income = float(line.strip())
        yield "max", income

    def reducer(self, key, values):
        max=0
        for value in values:
          if value>max:
            max=value
        max_income=max
        #method 2
        #max_income = max(values)
        yield key, max_income

if __name__ == '__main__':
    Maximum.run()
