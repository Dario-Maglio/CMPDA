#include <stdio.h>
#include <stdbool.h>
#define X 3
#define N 5

void Stampa(int a[X][X], int b[X][X]){
 printf("   1 2 3\n  _______\n");
 for (int i=0;i<X;i++){
   printf ("%d |",i+1);
   for (int j=0;j<X;j++){
     if (a[i][j]==1)
      printf ("a ");
     else if (b[i][j]==1)
      printf ("b ");
     else
      printf ("0 ");
   }
   printf ("\n");
 }
 printf ("\n");
}

_Bool Inserimento_T (char g,int k, int a[X][X],int b[X][X]) {
 int i,j,r,c;
 _Bool Sw;
 printf("Giocatore %c\nInserire le coordinate dello spazio da riempire:\nRiga: ",g);
 scanf ("%d",&i);
 r=i-1;
 printf("Colonna: ");
 scanf ("%d",&j);
 c=j-1;
 if ((b[r][c]==1)||(a[r][c]==1)) {
   printf("Errore: posizione già occupata.\nRiprova...\n");
   return Inserimento_T(g,k,a,b);
 }else{
   a[r][c]=1;
   if (k>2)
   //Controllo tris e return
   for (Sw=1,i=r,j=0;j<X;j++){//Controllo riga
     Sw*=a[i][j];
   }
   if (Sw==0){
     for (Sw=1,j=c,i=0;i<X;i++){//Controllo colonna
       Sw*=a[i][j]; 
     }
     if (Sw==0){//Controllo diagonali
       Sw=(a[2][0]*a[1][1]*a[0][2])+(a[0][0]*a[1][1]*a[2][2]);
     } 
     return Sw;
   }else
     return 0;
 }
} 

int main(void){
 _Bool sw; 
 int a[X][X]={0},b[X][X]={0},k;
 char g;
 printf ("La scacchiera iniziale è così rappresentata:\n\n");
 Stampa(a,b);
 for (k=1;(k<=N)&&(sw==0);k++){
  g='a';
  sw= Inserimento_T(g,k,a,b);
  Stampa(a,b);
  if ((k==N)||(sw==1)) 
    break;
  g='b';
  sw= Inserimento_T(g,k,b,a);
  Stampa(a,b);
 } 
 if (sw) 
  printf ("Ops, giocatore '%c' ha fatto tris :)\n",g);
 else
  printf ("Che scarsi... pareggio...\n");
 return 0;
}

