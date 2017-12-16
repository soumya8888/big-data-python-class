import mrjob
from mrjob.job import MRJob
import re
from itertools import islice, izip
import itertools

WORD_RE = re.compile(r'[a-zA-Z]+')

class BigramCount(MRJob):
  OUTPUT_PROTOCOL = mrjob.protocol.RawProtocol

  def mapper(self, _, line):
    words = WORD_RE.findall(line)

    for i in izip(words, islice(words, 1, None)):
      bigram=str(i[0]+ " " +i[1])
      yield (bigram, 1)

  def combiner(self, bigram, counts):
    yield (bigram.encode('utf-8'), sum(counts))

  def reducer(self, bigram, counts):
    yield (bigram.encode('utf-8'), str(sum(counts)))

if __name__ == '__main__':
  BigramCount.run()