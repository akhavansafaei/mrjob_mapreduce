
from mrjob.job import MRJob

class TotalIncomes(MRJob):

    def mapper(self, _, line):
        income = float(line.strip())
        yield "total", income

    def reducer(self, key, values):
        total = sum(values)
        yield key, total

if __name__ == '__main__':
    TotalIncomes.run()
