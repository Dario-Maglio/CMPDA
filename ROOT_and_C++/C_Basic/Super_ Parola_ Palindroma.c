#include <stdio.h>
#include <stdbool.h>
#define N 50

bool Palindroma (char a[], int i, int j){
 return (i>=j)? true : (a[i]==a[j])&&Palindroma(a,i+1,j-1);
}

void Stampa_inverso (char a[], int i, int j){
 if (j==i){
  putchar(a[i]);
  putchar('\n');
 }else{
  putchar(a[j]);
  Stampa_inverso(a,i,j-1);
 }
}

int main(void){
 int i=-1;
 char ch, a[N];
 printf("Inserisci una parola (massimo 50 caratteri): ");
 while ((ch=getchar())!='\n'){
  a[++i]=ch;
 }
 printf ("La parola inserita ");
 if (Palindroma(a,0,i))
  printf("e' palindorma.\n");
 else
  printf("non e' palindroma.\nL'inverso e' ");
 Stampa_inverso (a,0,i);
 return 0;
}


