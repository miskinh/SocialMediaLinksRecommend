import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities
from operator import itemgetter
import string

table = string.maketrans("","")

#import sys for file input output
import sys

class FormatCorpus(object):

	"""
 		FormatCorpus is used to format the input corpus for the LDA algorithm.
 		The output should be a .dat file.

  	"""

	def __init__(self,argv):
		self.dictionary = corpora.Dictionary([[i.replace('\n','') for i in open(argv[0]).readlines()]])
		self.corpusFile = argv[1]
		self.formattedFile = argv[2]

	def __iter__(self):
		"""
			Iterator function to iterated over each word of the corpus
    	"""
		for line in open(self.corpusFile):
			yield self.dictionary.doc2bow(line.lower().split())

	def format(self):
		"""
			Formats the corpus in the Blei format for teh LDA algorithm
    	"""
		corpus_memory_friendly = FormatCorpus(sys.argv[1:])
		corpus = [text for text in corpus_memory_friendly]
		corpora.BleiCorpus.serialize(self.formattedFile, corpus)

if __name__ == "__main__":
	ff = FormatCorpus(sys.argv[1:])
	ff.format()