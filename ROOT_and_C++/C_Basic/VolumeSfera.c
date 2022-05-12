#include <stdio.h>
#define CONSTANT (4.0f/3.0f)*3.1416f
int main(void){
float raggio;
printf("Inserisci il raggio della sfera: ");
scanf("%f",&raggio);
printf("Il volume e‘: %f\n", CONSTANT*raggio*raggio*raggio);
return 0;
}
