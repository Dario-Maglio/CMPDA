#include<stdio.h>

void carica (int n, int m, int a[][m]);
void stampa (int n, int m, int a[][m]);
void trasposta (int n, int m, int t[][n], int a[][m]);
void stampa_t (int n, int m, int a[][n]);

int main (void) 
{
	int n,m;
	printf("inserire numero righe: ");
	scanf("%d", &n);
	printf("inserire numero colonne: ");
	scanf("%d", &m);
	int a[n][m];
	carica (n,m,a);
        stampa (n,m,a);
	int t[m][n];
	trasposta (n,m,t,a);
        stampa_t (n,m,t);
}

void carica (int n, int m, int a[][m])
{
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<m; j++)
	    {
                 printf("inserire prossimo valore: ");
		 scanf("%d", & a[i][j]);
            }
         }
	 printf("\n");
}

void stampa (int n, int m, int a[][m])
{
        for (int i=0; i<n; i++)
        {
              for (int j=0; j<m; j++)
              {
                 printf("%d ", a[i][j]);
              }
              printf("\n");
        }
	printf("\n");
}

void trasposta (int n, int m, int t[][n], int a[][m])
{
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<m; j++)
	    {
             	 t[j][i]=a[i][j];
	    }
        }
}

void stampa_t (int n, int m, int a[][n]){
	for (int i=0; i<m; i++)
        {
              for (int j=0; j<n; j++)
              {
                 printf("%d ", a[i][j]);
              }
              printf("\n");
        }
	printf("\n");
}

	
		 
                 
    
