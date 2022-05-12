#include <stdio.h>
#define N 20

int regolare (int *a, int n, int x);
void occorrenze(int *a, int n, int p, int q, int *x, int *y);
int substr(char *s, char *t);

int main (void){
	int x=4,a[N]={11,11,11,2,4,1,2,2,6,3,21,25,3,4,5,3,8,2,4,4};
	if (x<2)
		return 1;
	if (regolare(a,N,x))
		printf ("La sequenza e' %d-regolare.\n",x);
	else
		printf ("La sequenza non e' %d-regolare.\n",x);
		
	//terzo esercizio
	x=0;
	int p=11,q=2,y=0;
	occorrenze(a,N,p,q,&x,&y);
	printf("Il numero di occorrenze di %d e' %d, mentre quello di %d e' %d\n", p,x,q,y);
	
	//quarto esercizio
	char *s="Buonaserasamiso",*t="so";
	if(substr(s,t))
		printf("%s contiene %s come sottostringa.\n",s,t);
	else
		printf("%s non contiene %s come sottostringa.\n",s,t);	
}



int regolare (int *a, int n, int x){
 int c,i=0;	
 for (;(a[i]!=x)&&(i<n); i++)
 	;
 	
 if (i==n)
 	return 0;
 else{
 	for (c=i++;(a[i]!=x)&&(i<n);i++)
 		;
 	if ((i==n)||((i-c)<=x))
 		return 0;
 	else{
 		for (c=2,i++;i<n;i++){
 			if(a[i]==x)
 				c++;	
 		}
	} 
  return (c==x)?x:0;
 }
}



void occorrenze(int *a, int n, int p, int q, int *x, int *y){
 if (n>=0){
 	occorrenze(a,n-1,p,q,x,y);
 	if (a[n]==p) 
 		(*x)++;
 	if (a[n]==q) 
 		(*y)++;
 }
}



int substr(char *s, char *t){
	for (;(*s!=*t)&&(*s!='\0');s++)
		;
	if (*s=='\0')
		return 0;
	else{
	  char *ss=s, *tt=t;
		for (;(*ss==*tt)&&(*ss!='\0');ss++,tt++)
			;
		if (*tt=='\0') 
			return 1;
		else
			return substr(s+1,t);
	}
}








