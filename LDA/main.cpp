#include <iostream>
#include <string>
#include <fstream>
#include "lda.h"
<<<<<<< HEAD
#define NO_DOCUMENTS 3
=======
#define NO_DOCUMENTS 5
>>>>>>> 85cfbb838227a8bae61dd1c8a3783c989a2130e6

using namespace std;

int main(){

	int noTopics = 5;

	string documents[NO_DOCUMENTS];

	documents[0] = "the dog and the cat decided to go for walk in the park together";
	documnets[1] = "scientist have discovered the large clouds of helium kill crops";
	documents[2] = "ben and jerrys ice cream is the great thing in the world because you can use in the park park to fill helium ballons";
	
	Lda l(NO_DOCUMENTS,documents,noTopics);

	l.outputDocuments();

	l.algorithm(20);

	l.outputTopicWordAssignment(cout);

	l.outputWordsInEachTopic(cout);

	return 0;
}
