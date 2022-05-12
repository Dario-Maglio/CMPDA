#include<stdio.h>
#define K_K 273.15f

int main(void){
 float K,C;
 printf("Immettere gradi Celsius: ");
 scanf("%f",&C);
 K=C+K_K;
 printf("I gradi Kelvin corrispondenti sono: %f\n", K);
 return 0;
}
