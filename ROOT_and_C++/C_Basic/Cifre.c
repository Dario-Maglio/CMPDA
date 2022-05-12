#include<stdio.h>

int main (void) {
 int n,i=0;
 printf("Inserisci il numero: ");
 scanf("%d", &n);
 do {
  n/=10;
  i++;
 }while (n>0);
 printf("Il numero di cifre è: %d\n",i);
 return 0;
}

