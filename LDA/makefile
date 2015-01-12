lda: main.o lda.o
	g++ -Wall -g main.o lda.o -o lda

main.o: main.cpp lda.h
	g++ -Wall -g -c main.cpp

lda.o: lda.cpp lda.h
	g++ -Wall -g -c lda.cpp

clean:
	rm -f *.o lda