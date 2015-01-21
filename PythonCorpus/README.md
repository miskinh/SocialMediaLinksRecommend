#MakeDictionary.py

This is a python script to make a custom dictionary from a given corpus. 
The script uses TF-IDF to decide which words in the corpus are most valuable and hold the most information.

##MakeDictionary.run

This is a small script to show how the file is run.
The command line inputs are the corpus.txt and dictionary.txt files that are to be generated.
The other inputs are the text files containing the individual documents.
After running, corpus.txt will hold each documment, one per line, and dictionary will hold the dictionary words.

#FormatCorpus

This is a python script to format the corpus.txt file to corpus.dat file that will be used in the LDA implementation.
The format for the corpus is as follows:
```
  [No words in document1] [term1]:[term1count] [term2]:[term2count] [term2]:[term2count]
  [No words in document2] [term1]:[term1count] [term2]:[term2count] [term2]:[term2count]
  .
  .
  .
```

##MakeDictionary.run

This is a small script to show how the file is run.
The command line inputs are the corpus.txt and dictionary.txt and corpus.dat.
corpus.txt and dictionary.txt were generated from MakeDictionary.py. corpus.dat is the output filename.
