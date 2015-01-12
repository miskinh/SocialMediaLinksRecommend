#include <iostream>
#include <string>
#include <fstream>
#include "lda.h"
#define NO_DOCUMENTS 5

using namespace std;

int main(){

	int noTopics = 5;

	string documents[5];

	Lda l(NO_DOCUMENTS,documents,noTopics);

	l.outputDocuments();

	l.algorithm(20);

	l.outputTopicWordAssignment(cout);

	l.outputWordsInEachTopic(cout);

	return 0;
}