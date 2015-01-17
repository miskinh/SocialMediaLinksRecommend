#include <fstream>
#include <cstring>

using namespace std;

int main(int argv, char* argc[]){
	ifstream in1,in2;
	ofstream out;
	char ch,word1[80],word2[80];
	for(int i = 0; i < argv; i++){
		in1.open(argc[i]);
		int length = strlen(argc[i]);
		//make new file
		char* newName = new char[length+6];
		strcpy(newName,argc[i]);
		strcat(newName, ".json");
		out.open(newName);

		in1.get(ch);
		int j = 0;

		while(!in1.eof()){
			if(isalpha(ch)){
				word1[j++] = ch;
			}
			else if(ch == ' '&& !strcmp(word1,"")){

			}
			else{
				in2.open("dictnostops.txt");
				word1[j] = '\0';
				int index = 0, result = -1;
				in2.getline(word2,80);
				while(!in2.eof()){
					if(!strcmp(word1,word2)){
						result = index;
						break;
					}
					in2.getline(word2,80);
					index++;
				}
				if(result > -1){
					out << result;
					out.put('\n');
				}
				in2.close();
				j = 0;
			}
			in1.get(ch);
		}
		in1.close();
		out.close();
		delete [] newName;
	}
}
