#include <stdio.h>
#define LIMIT 1023

int main (void){
 int Max=LIMIT,Min=0,C,ch,I=0;
 printf("Pensa ad un numero da 1 a 1023.\n");
 while (Max-Min>1){
  I++;
  C=(Max+Min)/2;
  printf ("%d.)Il tuo numero è %d? \nSe si, allora ho finito (f), altrimenti:\nil numero pensato è maggiore di %d?(s/n)\n",I,C,C);
  ch = getchar();
  getchar();
  if (ch=='f') 
   break;
  else if (ch=='s')
   Min=C;
  else
   Max=C;
 }
 if (ch=='f')
  printf ("Il numero pensato e': %d\n",C);
 else
  printf ("Il numero pensato e': %d\n",C+1);
 return 0;
}
