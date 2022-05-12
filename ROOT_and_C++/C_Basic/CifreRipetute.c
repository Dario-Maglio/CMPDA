#include <stdio.h>

int main (void) {
 long N;
 int Max,I,CV[10]={0},K,Sw=0;
 printf("Inserire il numero con al massimo 9 cifre: ");
 scanf ("%ld",&N);
 while (N!=0) {
  I=N%10;
  CV[I]+=1;
  N/=10;
  if (CV[I]>1) 
   Sw=1;
 }
 if (Sw==0)
 printf ("Non ci sono cifre ripetute.\n");
 else{
  Max=CV[0];
  K=0;
  for (I=1;I<10;I++){
   if (CV[I]>Max){
     Max=CV[I];
     K=I;
   }
  }
  printf ("La cifra che si e' ripetuta di più, e' '%d'.\nEssa si e' ripetuta %d volte.\n",K,Max);
 }
 return 0;
}
