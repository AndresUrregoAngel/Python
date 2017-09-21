from mrjob.job  import MRJob
from mrjob.step import MRStep
import re


WORD_RE = re.compile(r"[\w']+")

class MostPopularMovie(MRJob):
    def steps(self):
        return [
            MRStep (mapper = self.mapper_get_rating,
                    reducer = self.reducer_count_rating),
            MRStep (mapper= self.mapper_passthrough,
                    reducer = self.reducer_find_max)
        ]

    def mapper_get_rating(self, _, line):
        (userID,movieID, rating, timestamp) = line.split('\t')
        yield movieID,1

    def reducer_count_rating (self, key, values):
        yield None, (sum(values), key)

    def mapper_passthrough (self,key  , value ):
        yield key,value


    def reducer_find_max (self, key, values):
        yield max(values)


if __name__ == '__main__':
    MostPopularMovie.run()





