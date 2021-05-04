#include<stdio.h>
#define BISESTILIT 4
#define PERCENTUALE 100

int main (void) {
 int A,Sec,NSec,D4,D400,T;
 printf("Inserire anno da verificare: ");
 scanf("%d",& A);
 Sec=1/((A%PERCENTUALE)+1);
 D400=1/((A%(BISESTILIT*PERCENTUALE))+1);
 D4=1/((A%BISESTILIT)+1);
 NSec=-(Sec-1);
 T=(Sec*D400)+(NSec*D4);
 printf("Considerato l'anno %d, se il risultato e' 1, allora e' bisestile,\naltrimenti, se il risultato e' 0, allora e' normale. \nIl risultato e': %d\n",A,T);
 return 0;
}
