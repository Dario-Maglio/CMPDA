#include <stdio.h>
#include <string.h>
#define N 15

void Stampa_stringhe(int n,char a[][N]){
	for (int i=0; i<n; i++)
		printf ("%s\n",a[i]);
}

void Ordinamento (int n,char a[][N]){	
	if (n!=0){
		Ordinamento(--n,a);
		if (strcmp(a[n-1],a[n])>0){
			char b[N];
			strcpy(b,a[n--]);
			while ((n>=0)&&(strcmp(a[n],b)>0)){
					strcpy(a[n+1],a[n]);
					n--;
			}
			strcpy (a[n+1],b);
		}
	

	}
}

int main (int argc,char* argv[]){
	if (argc<2) return -1;	
	int n=argc-1;
	char a[n][N];
	for (int i=0;i<n; i++){
		strcpy (a[i],argv[i+1]);
	}
	Ordinamento(n,a);
	Stampa_stringhe(n,a);
	return 0;	
}
