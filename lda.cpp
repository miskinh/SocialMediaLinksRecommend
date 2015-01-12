#include <iostream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <iomanip>

#include "lda.h"

using namespace std;

Lda::Lda(int noDocuments, string inputDocuments[], int noTopics){
	K = noTopics;

	M = noDocuments;

	//only first index can have dynamic size int[M][K]
	N = new int* [M];

	assignment = new int* [M];

	alpha = 50.0/K;
	beta = 0.1;

	documents = new string[noDocuments];

	for(int i = 0; i < M; i++){
		documents[i] = inputDocuments[i];
		int numWords = countWords(documents[i]);
		assignment[i] = new int[numWords];
		N[i] = new int[K];
		for(int topic = 0; topic < K; topic++)
			N[i][topic] = 0;
	}
}

Lda::~Lda(){
	delete [] documents;
	for(int i = 0; i < M; i++){
		delete N[i];
		delete assignment[i];
	}
	delete N;
	delete assignment;
	for(map<string,int*>::iterator it = v.begin(); it != v.end(); ++it)
		delete it->second;
}

void Lda::outputDocuments(){
	for(int i = 0; i < M; i++){
		cout << documents[i];
		cout << " " << countWords(documents[i]) << endl;
	}
	cout << endl;
	return;
}

int Lda::countWords(string document){
	int i = 0, count = 0;
	while(document[i] != '\0'){
		if(document[i] == ' ')
			count++;
		i++;
	}
	if(i > 0)
		count++;
	return count;
}

void Lda::algorithm(int noRepetitions){
	for(int i = 0; i < noRepetitions; i++){
		//iteratate through documents
		for(int d = 0; d < M; d++){
			int noWords = countWords(documents[d]);
			//iterate over words
			istringstream iss(documents[d]);
			string token;
			for(int n = 0; n < noWords; n++){
				iss >> token;
				//if the first iteration through the algorithm
				if(i == 0){
					//create new entry in v if none already
					map<string,int*>::iterator it = v.find(token);
					if(it == v.end()){
						v[token] = new int[K];
						for(int index = 0; index < K; index++)
							v[token][index] = 0;
					}
					int topic = rand() % K;
					assignment[d][n] = topic;
					v[token][topic]++;
					N[d][topic]++;
				}
				//if not the first iteration
				else{
					//unassign word
					int assignedTopic = assignment[d][n];
					v[token][assignedTopic]--;
					N[d][assignedTopic]--;

					//find new best topic assignment based on rest of document
					double* scores = new double[K];
					int best = 0;
					for(int z = 0; z < K; z++){
						scores[z] = calculateStatistic(z,token,d);
						if(z > 0){
							if(scores[z] > scores[z-1])
								best = z;
						}
					}
					//make new assignment
					v[token][best]++;
					N[d][best]++;
					assignment[d][n] = best;
				}
			}
		}
	}
	return;
}

void Lda::outputTopicWordAssignment(ostream& out){
	for(int d = 0; d < M; d++){
		int numWords = countWords(documents[d]);
		istringstream iss(documents[d]);
		string token;
		for(int n = 0; n < numWords; n++){
			iss >> token;
			out << token << "(" << assignment[d][n] <<") ";
		}
		out << endl;
	}
	out << endl;
	return;
}

void Lda::outputWordsInEachTopic(ostream& out){
	for(map<string,int*>::iterator it = v.begin(); it != v.end(); ++it){
		out << setw(20)<< it->first << "\t";
		for(int topic = 0; topic < K; topic++){
			cout << it->second[topic] << "\t";
		}
		out << endl;
	}
	out << endl;
	return;
}

double Lda::calculateStatistic(int topic, string word, int document){
	double denominator1 = 0.0;
	for(int i = 0; i < K; i++){
		denominator1 += N[document][i];
		denominator1 += alpha;
	}
	double numerator1 = N[document][topic] + alpha;
	double denominator2 = 0.0;
	for(int d = 0; d < M; d++){
		int numWords = countWords(documents[d]);
		istringstream iss(documents[d]);
		string token;
		for(int n = 0; n < numWords; n++){
			iss >> token;
			denominator2 += v[token][topic];
			denominator2 += beta;
		}
	}
	double numerator2 = v[word][topic] + beta;

	return (numerator1/denominator1)*(numerator2/denominator2);
}
