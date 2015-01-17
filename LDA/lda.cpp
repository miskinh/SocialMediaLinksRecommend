#include <iostream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <iomanip>
#include <fstream>

#include "lda.h"

using namespace std;

Lda::Lda(int noDocuments, char* inputDocuments[], int noTopics){
	K = noTopics;

	M = noDocuments;

	N = new int* [M];

	assignment = new int* [M];

	alpha = 50.0/K;
	beta = 0.1;

	documents = new char* [noDocuments];

	for(int i = 0; i < M; i++){
		int fileNameLength = strlen(inputDocuments[i]);
		documents[i] = new char[fileNameLength+1];
		strcpy(documents[i],inputDocuments[i]);
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
	delete [] N;
	delete [] assignment;
	for(map<int,int*>::iterator it = v.begin(); it != v.end(); ++it)
		delete [] it->second;
}

int Lda::countWords(const char* filename){
	int numWords = 0;
	fstream in(filename);
	std::string unused;
	while ( std::getline(in, unused) )
   		++numWords;
   	in.close();
   	return numWords;
}

void Lda::algorithm(int noRepetitions){
	ifstream in;
	ofstream out;

	for(int i = 0; i < noRepetitions; i++){
		for(int d = 0; d < M; d++){
			in.open(documents[d]);
			int word;
			//first iteration
			if(i == 0){
				int n = 0;
				in >> word;
				while(!in.eof()){
					map<int,int*>::iterator it = v.find(word);
					if(it == v.end()){
						v[word] = new int[K];
						for(int index = 0; index < K; index++)
							v[word][index] = 0;
					}
					//get the next topic
					int topic = rand() % K;
					assignment[d][n] = topic;
					v[word][topic]++;
					N[d][topic]++;
					n++;
					in >> word;
				}
			}else{
				int n = 0;
				in >> word;
				while(!in.eof()){
					//unassign word
					int assignedTopic = assignment[d][n];
					v[word][assignedTopic]--;
					N[d][assignedTopic]--;

					double* scores = new double[K];
					int best = 0;

					for(int z = 0; z < K; z++){
						scores[z] = calculateStatistic(z,word,d);
					}
					for(int z = 0; z < K; z++){
						if(scores[best] < scores[z]){
							best = z;
						}
					}
					//make new assignment
					v[word][best]++;
					N[d][best]++;
					assignment[d][n] = best;
					n++;
					in >> word;
				}
			}
			in.close();
		}
	}
	out.close();
	return;
}

void Lda::outputTopicWordAssignment(ostream& out){
	for(int d = 0; d < M; d++){
		int nextWord;
		ifstream in(documents[d]);
		in >> nextWord;
		int n = 0;
		while(!in.eof()){
			out << nextWord << "(" << assignment[d][n] <<") ";
			in >> nextWord;
			n++;
		}
		in.close();
	}
	out << endl;
	return;
}

void Lda::outputWordsInEachTopic(ostream& out){
	out << setw(20) << " ";
	for(int topic = 0; topic < K; topic++){
		out << "Topic " << topic << "\t";
	}
	out << endl;

	for(map<int,int*>::iterator it = v.begin(); it != v.end(); ++it){
		out << setw(20)<< it->first << "\t";
		for(int topic = 0; topic < K; topic++){
			out << it->second[topic] << "\t";
		}
		out << endl;
	}
	out << endl;
	return;
}

double Lda::calculateStatistic(int topic, int word, int document){
	double denominator1 = 0.0;
	for(int i = 0; i < K; i++){
		denominator1 += N[document][i];
		denominator1 += alpha;
	}
	double numerator1 = N[document][topic] + alpha;
	double denominator2 = 0.0;
	for(int d = 0; d < M; d++){
		int nextWord;
		ifstream in(documents[d]);
		in >> nextWord;
		while(!in.eof()){
			denominator2 += v[nextWord][topic];
			denominator2 += beta;
			in >> nextWord;
		}
		in.close();
	}
	double numerator2 = v[word][topic] + beta;

	return (numerator1/denominator1)*(numerator2/denominator2);
}
