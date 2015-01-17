#include <fstream>
#include <cstring>

using namespace std;

int main(int argc, char* argv[]){
	ifstream in;
	ofstream out;
	for(int i = 0; i < argc; i++){
		//open file
		in.open(argv[i]);
		int length = strlen(argv[i]);
		//make new file
		char* newName = new char[length+8];
		strcpy(newName,"simple-");
		strcat(newName,argv[i]);
		out.open(newName);
		char ch;
		in.get(ch);
		while(!in.eof()){
			if(isalpha(ch) || ch == ' '){
				out.put(tolower(ch));
			}
			in.get(ch);
		}
		in.close();
		out.close();
		delete [] newName;
	}
}