#include <stdio.h>

//void carica (int n, int a[n]);
void carica_r (int n, int a[n]);
//void stampa (int n, int a[n]);
void stampa_r (int n, int a[n]);
//void ordinamento (int n, int a[n]);
void ordinamento_r (int n, int a[n]);

int main(void)
{
	int n;
	printf("inserire la dimensione del vettore\n");
  	scanf("%d", &n);
        int a[n];
        carica_r (n,a);
	stampa_r (n,a);
	printf("\n");
	ordinamento_r (n,a);
        stampa_r (n,a);
	printf("\n");
	return 0;
}

/********************************************************
*void carica (int n, int a[n])				*
*{							*
*	for(int i=0; i<n; i++)				*
*        {						*
*            printf("inserire prossimo valore\n");	*
*            scanf("%d",&a[i]);				*
*        }						*
*}							*
* 							*
*void stampa (int n, int a[n])				*
*{							*
*	for(int i=0; i<n; i++)				*
*	{						*
*	    printf("%d ", a[i]);			*
*        }						*
*        printf("\n");					*
*}							*
*							*
*void ordinamento (int n, int a[n])			*
*{       						*
*       int i,x,j;					*
*	for (j=1; j<n;j++)				*
*        {						*
*	    x=a[j];					*
*	    for (i=j-1; x<a[i]; i--)			*
*            {						*
*                a[i+1]=a[i];				*
*            }						*
*	    a[i+1]=x;					*
*        }						*
*}							*
*							*
********************************************************/

void carica_r (int n, int a[n]){
	if (n==1){
		printf("inserire prossimo valore\n");
        	scanf("%d",&a[n-1]);
	}else{
		carica_r(n-1,a); 
        	printf("inserire prossimo valore\n");
        	scanf("%d",&a[n-1]);
	}
}

void stampa_r (int n, int a[n]){
	if (n==1){
		printf("%d ", a[n-1]);
	}else{
		stampa_r(n-1,a); 
        	printf("%d ", a[n-1]);
	}
}

/* In carica e stampa ricorsivi si scrive caso base e passo induttivo in questo modo per evidenziare il funzionamento di una ricorsione. Invece, nel caso seguente si utilizza solo il passo induttivo sfruttando il fatto che la chiamata a funzione del caso base non ha istruzioni (caso base n==o)*/

void ordinamento_r (int n, int a[n]){
       if (n>0) {
           ordinamento_r(n-1,a);
	   int i,x;
   	   x=a[n];					
	   for (i=n-1; x<a[i]; i--) {					
                a[i+1]=a[i];				            
           }					
            a[i+1]=x;		
        }		
}




/********************************************************
*void ordinamento_puntatori (int n, int *a){		*
*	int *b=a+1,*q,x;				*
*	for (int *p=b+n; b<p; b++)			*
*        {						*
*	    x=*b;					*
*	    for (q=b-1; (x<*q)&&(q>=a); q--)		*
*            {						*
*                *(q+1)=*q;				*
*            }						*
*	    *(q+1)=x;					*
*        }						*
*}							*
*							*
********************************************************/



