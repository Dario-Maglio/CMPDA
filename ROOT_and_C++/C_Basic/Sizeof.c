#include <stdio.h>
#include <string.h>
#define N 15

int main (int argc,char* argv[]){
	if (argc<2) return -1;
	int b[N];
	int i,n=argc-1;
	char a[n][N];
	for (i=0;i<n; i++){
		strcpy (a[i],argv[i+1]);
	}
	for (i=0;i<n; i++){
		printf ("%d %s\n%d %s\n", strlen(argv[i]), argv[i],sizeof(a[i]), a[i]);
	}
	printf ("%d %s\n", strlen(argv[i]), argv[i]);  
	/*La dimensione di sizeof(argv[i]) restituisce sempre 4. 
	Probabilmente perchè essendo argv[i] un puntatore ad una stringa letterale, 
	quello che viene letto è il numero di byte che occupa il puntatore.
	Diversamente, le stringhe letterali, essendo degli array monodimensionali, 
	vengono interpretati come tali, e viene quindi letta la dimensione totale dell'array, non della stringa. 
	Invece con sizeof(*argv[i]) viene stampato 1, ossia il numero di byte occupato dal carattere 
	allocato all'indirizzo puntato. Per ottenere l'effettiva lunghezza di una stringa, usiamo strlen.*/
	printf ("%d %d %d %d %d\n", sizeof(*argv[i]),sizeof(a[i-1][0]),sizeof(argv[i]),sizeof(a[i-1]),sizeof(b));
	return 0;	
}
