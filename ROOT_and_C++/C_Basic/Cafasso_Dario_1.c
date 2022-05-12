#include <stdio.h>
#include <stdlib.h>
#define N 20


void punte (int *a, int n){
	n-=2;
	while(n-->0){
		if ((a[n]==a[n+2])&&(a[n+1]>a[n]))
			printf ("(%d,%d,%d)\n",a[n],a[n+1],a[n+2]);
	}

}

int main(int argc, char *argv[]){
	if (argc<3) 
		return 1;
	int i=0,a[N];
	for (;i<(argc-1);i++){
		a[i]=atoi(argv[i+1]);
	}
	punte(a,i);
	return 0;
}


