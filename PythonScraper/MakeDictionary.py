import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities
from operator import itemgetter
from Data.Return import Return
from Data.Models import *
import sys

#database = MySQLDatabase('SocialMedia', **{'host': 'localhost', 'password': 'nimandian10', 'user': 'root'})

PUNCTUATION = "!\"#$%&'()*+,./:;<=>?@[\]^`{|}~0123456789\n\t"

def deleteContent(pfile):
	"""
		Deletes the content of a file.
   	"""
	pfile.seek(0)
	pfile.truncate()

def remove_non_ascii(text):

    return ''.join(i for i in text if ord(i)<128)

def replacePunctuation(line):
	"""
		Replaces the punctuation of the file with spaces.
	"""
        for i in PUNCTUATION:
                try:
                        line = line.replace(i," ")
                except AttributeError:
                        return "VOID"        
        line = remove_non_ascii(line)
        return line


def format_corpus():
	"""
		Removes punctuation and returns array of lower case strings for the corpus.
   	"""
   	dataReturn = Return()
   	documents = dataReturn.getDocuments()
        #print(documents)
   	texts = []
        for document in documents:
                document = replacePunctuation(document)
                #print(document)
                if document != "VOID":
                        text = document.lower().split()
                        texts.append(text)
        return texts


def make_dictionary_from_corpus(NUM_TERMS):                            
        """                                                                                                                                                                              
                Makes the dictionary file. The number of words is NO_TERMS.                                                                                                            
                Uses tfidf to determine if a word shold be included in a dictionary.                                                                                                            
        """  
        num_terms = int(NUM_TERMS)
        texts = format_corpus()

	dictionary = corpora.Dictionary(texts)
	corpus = [dictionary.doc2bow(text) for text in texts]
	tfidf = models.TfidfModel(corpus)
	corpus_tfidf = tfidf[corpus]

	dict_corpus_tfidf = []
	for doc in corpus_tfidf:
		for (word1,freq1) in doc:
			not_in_dict = True
			for(word2,freq2) in dict_corpus_tfidf:
				if(word1 == word2):
					not_in_dict = False
					if(freq1 > freq2):
						freq2 = freq1
					break
			if(not_in_dict):
				dict_corpus_tfidf.append((word1,freq1))

        
        database.connect()
        database.drop_table(Dictionary,True)
        database.create_table(Dictionary)

	sorted_corpus_tfidf = sorted(dict_corpus_tfidf,key=itemgetter(1),reverse=True)

	dictid = [id for (id,freq) in sorted_corpus_tfidf]
	dictWords = [word for word,id in dictionary.token2id.items() if id in dictid]
	with open("dictionary.txt", "a") as outputFile:
		deleteContent(outputFile)
		i = 0
		for word in dictWords:
                        #print(word)
			if i == num_terms:
				break
			if(len(word) > 2):
				try:
                                        Dictionary.create(word = word)
                                        outputFile.write(word)
                                        outputFile.write('\n')
                                        i += 1
                                except UnicodeEncodeError:
                                        j = 0
                                        
        database.close()
                                        
if __name__ == "__main__":
        if(len(sys.argv) < 2):
                print("Usage: MakeDictionary.py <NO_TERMS>")
        else:
                make_dictionary_from_corpus(sys.argv[1])
