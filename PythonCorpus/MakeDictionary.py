import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


from gensim import corpora, models, similarities
from operator import itemgetter
import string

table = string.maketrans("","")

#import sys for file input output
import sys

class MakeDictionary:
	"""
 		MakeDictionary allows us to create our own dictionary based on the corpus we use.
 		Using tfidf the terms with the most information are put in the dictionary.

  	"""


	def __init__(self,argv):
		self.corpusFile = argv[0]
		self.dictFile = argv[1]
		self.num_terms = 1000

	def __iter__(self):
		"""
			Iterator function to iterated over each document of the corpus file
    	"""
		for line in open(self.corpusFile):
			yield line.translate(table, string.punctuation).lower().split()

	def make_documents_into_string(self,argv):
		"""
			Converts a corpus split into different files into a single file,
			where each line is a document.
    	"""
		with open(self.corpusFile, "a") as outputFile:
			for filename in argv:
				with open(filename, "r") as inputFile:
					outputFile.write(inputFile.read().replace('\n', ''))
					outputFile.write('\n')


	def make_dictionary_from_corpus(self):
		"""
			Makes the dictionary file. The number of words is self.num_terms.
			Uses tfidf to determine if a word shold be included in a dictionary.
    	"""

		corpus_memory_friendly = MakeDictionary(sys.argv[1:3])
		texts = [document for document in corpus_memory_friendly]
		dictionary = corpora.Dictionary(texts)
		corpus = [dictionary.doc2bow(text) for text in texts]
		tfidf = models.TfidfModel(corpus)
		corpus_tfidf = tfidf[corpus]

		dict_corpus_tfidf = []
		for doc in corpus_tfidf:
			for (word,freq) in doc:
				if any(word in code for code in dict_corpus_tfidf):
					continue
				dict_corpus_tfidf.append((word,freq))

		sorted_corpus_tfidf = sorted(dict_corpus_tfidf,key=itemgetter(1),reverse=True)
		dictid = [id for (id,freq) in sorted_corpus_tfidf[:self.num_terms]]
		dict = [word for word,id in dictionary.token2id.items() if id in dictid]

		with open(self.dictFile, "a") as outputFile:
			for word in dict:
				outputFile.write(word)
				outputFile.write('\n')


if __name__ == "__main__":
	mkd = MakeDictionary(sys.argv[1:3])

	mkd.make_documents_into_string(sys.argv[3:])
	mkd.make_dictionary_from_corpus()