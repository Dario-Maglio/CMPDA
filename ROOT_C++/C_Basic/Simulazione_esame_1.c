#include <stdio.h>
#include <stdlib.h>

void Interruzioni (int *a, int n);

int main (int argc, char *argv[]) {
    int n= argc-1, a[n];
    int i=1,*p=a;   
    for (;p<(a+n);p++,i++) {
        *p=atoi(argv[i]);
    }
    Interruzioni(a,n);
    return 0;
}

void Interruzioni (int *a, int n){
    int *p=a;
    while (p<(a+n-1)){
        if (*p>*(p+1)) 
            printf ("(%d,%d)\n",*p,*(p+1));
        p++;
    }
}
