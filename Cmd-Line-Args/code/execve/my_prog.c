#include <stdio.h>
#include <stdlib.h>

int main ( int argc, char *argv[], char *envp[])
{
	printf ("Arguments:\n");
	for ( int i = 1; i < argc; ++i){
		printf("\t argv[%d] -> %s \n", i, argv[i]);
	}
	
	printf ("\n\n");
}
