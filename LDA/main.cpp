#include <iostream>
#include <string>
#include <fstream>
#include "lda.h"

using namespace std;

int main(int argv, char* argc[]){

	ofstream out;
	out.open("topics.txt");

	int noTopics = 5;

	char** filenames = new char* [argv-1];

	for(int i = 1; i < argv; i++){
		filenames[i-1] = argc[i];
	}

	Lda l(argv-1,filenames,noTopics);

	l.algorithm(5);

	//l.outputTopicWordAssignment(out);

	l.outputWordsInEachTopic(out);

	out.close();

	return 0;
}
