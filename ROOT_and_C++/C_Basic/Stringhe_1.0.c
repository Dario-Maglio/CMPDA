#include <stdio.h>

int strcmp (char *p,char*q);

int main (int argc, char* argv[]){
 if (argc!=3){
   printf("Numero di elementi inseriti non corretto.\n");
   return 1;
 }
 if (strcmp(argv[1],argv[2]))
   printf("Le due stringhe non sono identiche. \n");
 else
   printf("Le due stringhe sono identiche.\n");
 return 0;
}

int strcmp (char *p,char*q){
 while((*p!='\0')&&(*q!='\0')){
   if (*p!=*q)
     return 0;
   p++;
   q++;
 }
 return ((*p!='\0')||(*q!='\0'))?0:1;
}

/****************************************
*#include<stdio.h>                      *
*					*
*int atoi (char *p);			*
*					*
*int main (int argc, char* argv[]){	*
*   int i, sum=0;			*
*   for (i=1;i<argc;i++)		*
*       sum+= atoi(argv[i]);		*
*   printf("Somma = %d\n",sum);		*
*   return 0;				*
*}					*
*					*
*int atoi (char *p){			*
* int k;				*
* for (;*p;p++)				*
*   k=10*k + *p-'0';			*
*  return k;				*
*}					*
****************************************/

