from mrjob.job import MRJob
from mrjob.step import MRStep

class TrigramCount(MRJob):

    def mapper(self, _, line):
        '''           
        This mapper gets one line, but has to yield trigrams on 
        this line and leftover words on previous lines. To manage
        the "leftover" words, a simple list is used, as an instance
        variable (which persists between mapper calls)
        '''
        try:
           T = self.TriGramList
        except:
           self.TriGramList = []
        # get all the words for this line and append to TriGramList
        if len(line.strip()) == 0:
           self.TriGramList = []  # consider this line to "break" text
           return  # ignore empty lines
        self.TriGramList.extend(line.split())
        # now generate all trigrams from the current list
        while len(self.TriGramList) > 2:
           T = ' '.join(self.TriGramList[:3])  # one trigram
           yield (T,1)
           self.TriGramList.pop(0)  # remove the first word from list

    def reducer(self, key, values):
        yield key, sum(values)

    def steps(self):
        return [ MRStep(mapper=self.mapper,
                 reducer=self.reducer) ]

if __name__ == '__main__':
    TrigramCount.run()