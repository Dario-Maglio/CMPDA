#include <stdio.h>

int main(void){
 char ch;
 printf("Inserisci il carattere: ");
 scanf("%c", &ch);
 if ('a'<= ch && ch<= 'z') 
  ch=ch-'a'+'A';
 printf("Il carattere maiuscolo è: %c\n", ch);
 return 0;
}

