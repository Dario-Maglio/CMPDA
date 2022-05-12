#include <stdio.h>
#define X 3

int main(void){
 typedef int Contatori,Interruttore,Salvataggi;
 int A[X][X]={0};
 Contatori I,J;
 Interruttore Sw;
 Salvataggi K,R,C;
 printf ("La scacchiera iniziale è così rappresentata:\n\n");
 //Stampa scacchiera
 printf("   1 2 3\n  _______\n");
 for (I=0;I<X;I++){
   printf ("%d |",I+1);
   for (J=0;J<X;J++){
     printf ("%d ", A[I][J]);
   }
   printf ("\n");
 }
 printf ("\n");
 //Inserimento coordinate
 printf("Inserire le coordinate dei 3 spazi da riempire:\n");
 for (K=1;K<=X;K++){
   printf("\nSpazio %d\nRiga: ",K);
   scanf ("%d",&I);
   printf("Colonna: ");
   scanf ("%d",&J);
   A[I-1][J-1]=1;
   if (K==1){//Salvataggio primo elemento
     R=I-1;
     C=J-1;
   }
 }
 //Stampa scacchiera
 printf("\n   1 2 3\n  _______\n");
 for (I=0;I<X;I++){
   printf ("%d |",I+1);
   for (J=0;J<X;J++){
     printf ("%d ", A[I][J]);
   }
   printf ("\n");
 }
 printf ("\n");
 //Tris migliorato
 for (K=1,I=R,J=0;J<X;J++){//Controllo riga
   K*=A[I][J];
 }
 Sw=K;
 if (Sw==0){
   for (K=1,J=C,I=0;I<X;I++){//Controllo colonna
     K*=A[I][J]; 
   }
   Sw=K;
   if (Sw==0){//Controllo diagonali
     Sw=(A[2][0]*A[1][1]*A[0][2])+(A[0][0]*A[1][1]*A[2][2]);
   }
 }
 if (Sw) 
   printf("C'E' UN TRIS!!!\n");
 else 
   printf("Non c'è un tris... :(\n");
 return 0;
}
