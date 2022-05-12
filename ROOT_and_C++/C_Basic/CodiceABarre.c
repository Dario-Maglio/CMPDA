#include<stdio.h>
int main (void) 
{
  int a,b,c,d,e,f,g,h,i,l,m,n,som1,som2,som;
  printf("inserisci sequenza di cifre: ");
  scanf("%1d%1d%1d%1d%1d%1d%1d%1d%1d%1d%1d%1d", &a, &b, &c, &d, &e, &f, &g, &h, &i, &l, &m, &n);
  som1=(a+c+e+g+i+m)*3;
  som2=b+d+f+h+l;
  som=som1+som2-1;
  som=9-(som%10);
  if (som==n)
     printf("Il codice a barre è non c'è male.\n");
  else
     printf("Il codice a barre fa cagare.\n");
return 0;
}


