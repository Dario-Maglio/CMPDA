#include<stdio.h>

int main (void){
 int N,I=0,K=1,C;
 printf("Inserisci il numero positivo: ");
 scanf("%d", &N);
 while (K<N) {
  C=K;
  K*=2;
  I++;
 }
 if (N==0)
  printf("Zero non e' potenza di 2.\n");
 else if (K==N)
  printf("Il numero è potenza di 2^%d\n", I);
 else
  printf("Il numero è 2^%d+(%d)\n", --I, (N-C));
 return 0;
}
