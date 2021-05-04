#include <stdio.h>

int main(void) {
 int d,N;
 printf("Inserire il numero: ");
 scanf("%d",&N);
 for (d=2;d<N;d++) {
  if (N%d==0) break;
 }
 if (d==N)
  printf("Il numero è primo.\n");
 else
  printf("Il numero non è primo.\n");
 return 0;
}
