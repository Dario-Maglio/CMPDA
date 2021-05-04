#include <stdio.h>

int main(int argc, char **argv)
{
	char **p=argv+1;
	for (; p<(argc+argv); p++)
		printf("%d)%s%s", p-argv, *p, (p< argv+argc-1) ? ";\n" : ".");
	printf("\n");
	return 0;
}


