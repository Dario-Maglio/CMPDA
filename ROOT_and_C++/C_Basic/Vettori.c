#include <stdio.h>
#include <ctype.h>

int main (void){
 //Inizializazione vettore
 char ch;
 typedef int Puntatori;
 Puntatori N,I,X,J;
 printf ("Inserire numero di elementi della lista: ");
 scanf ("%d", &N);
 int A[N];
 printf ("Inserire i %d elementi della lista:\n",N);
 for (I=0; I<N; I++) {
  scanf ("%d",&A[I]);
 }
 printf("\n");
 //Stampa del vettore
 printf ("I %d elementi della lista sono: ",N);
 for (I=0; I<N; I++) {
  printf ("%d ", A[I]);
 }
 printf("\n");
 //Ordinamento
 printf("La lista è tutta in ordine crescente eccetto l'ultimo elemento? (s/n) ");
 getchar();
 ch=getchar();
 if (ch=='s'){//Inserimento in lista
   I=N-1;
   X=A[I];
   while ((I>0)&&(A[I-1]>X)){
     A[I]=A[I-1];
     I--;
   }
   A[I]=X;
 }else{//Ordinamento completo "Insertion sort"
   for (I=1;I<N;I++){
     X=A[I];
     for (J=I;((J>0)&&(A[J-1]>X));J--){
     A[J]=A[J-1];
     }
   A[J]=X;
   } 
 }
 //Stampa del vettore
 printf ("I %d elementi della lista sono: ",N);
 for (I=0; I<N; I++) {
  printf ("%d ", A[I]);
 }
 printf("\n");
 return 0;
}
