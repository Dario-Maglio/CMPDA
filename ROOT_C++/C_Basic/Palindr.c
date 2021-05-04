#include <stdio.h>
#define A 50

int main (void){
	char a[A];
	int i;
	for (i=0; (a[i]=getchar())!='\n'; i++);
	int k=i;	
	for (i=0; i<=k;i++)
		printf("%c",a[i]);
	i=0;
	k--; 	
	while (i<=k){
		if (a[i++]!=a[k--])		
			break;
	}
	if (i>=k)
		printf ("Si\n");
	else
		printf ("No\n");

	return 0;
}
