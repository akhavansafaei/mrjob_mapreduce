
from mrjob.job import MRJob
from mrjob.step import MRStep

class GeneralizedMeanJob(MRJob):

    def mapper(self, _, line):
        income = float(line)
        yield None, income

    def reducer(self, _, incomes):
        # Replace 'p' with the desired order of the generalized mean
        p = 2  # You can change this value to calculate for different orders

        # Calculate the mean
        total = 0
        count = 0
        for value in incomes:
            total += value**p
            count += 1
        mean=(total/count)**(1/p)





        #incomes_list = list(incomes)
        #n = len(incomes_list)

        
        #mean = (sum(x**p for x in incomes_list) / n)**(1/p)

        yield None, mean

if __name__ == '__main__':
    GeneralizedMeanJob.run()

