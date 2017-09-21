from mrjob.job import MRJob

class MRCounter(MRJob):
    def mapper(self,key,line):
        (userID,movieID,rating,timestamp) = line.split('\t')
        yield rating,1

    def reducer(self,rating,occurence):
        yield rating, sum(occurence)


MRCounter.run()

