#include <stdio.h>

int regolare (int *a, int n, int x);
void trova_estremi (int *a, int n, int *min, int *max);
int suffix (char *s, char *t);

int main(void){
    int min, max, n=18,x=2;
    int a[]={4,11,43,3,2,4,5,2,5,6,2,90,12,5,65,8,23,5};
    if (regolare (a, n, x))
        printf("La sequenza è %d-regolare.\n",x);
    else
        printf("La sequenza non è %d-regolare.\n",x);
    trova_estremi(a,n,&min,&max);
    printf("Il massimo e'%d.\n",max);
    printf("Il minimo e'%d.\n",min);
    char s[]="maria",t[]="rosamaria";
    if (suffix(s,t))
	printf("%s e' suffisso di %s.\n",s,t);
    return 0;
}

int regolare (int *a, int n, int x){
    int i=0,k=1,*p;
    for(p=a; p<a+n; p++){
        if (*p==x) {
            while ((i<x)&&((p+x+1)<(a+n))){
                p+=x+1;
                k*=(*p==x);
                i++;
            }
            if (i==x)
                return k;
        }
    }
    return 0;
}

void trova_estremi (int *a, int n, int *min, int *max){
    if (n==1){
        *max=a[0];
        *min=a[0];
    }else{
        trova_estremi(a,n-1,min,max);
        if (*max< a[n-1])
            *max= a[n-1];
        if (*min> a[n-1])
            *min= a[n-1];
    }
}

int suffix (char *s, char *t){
    char *p=s;
    for (;*s;s++);
    for (;*t;t++);
    for (;((*s==*t)&&(s>=p));s--,t--)
	;
    return (s<p)?1:0;
}






