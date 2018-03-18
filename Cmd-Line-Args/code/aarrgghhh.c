#include<stdio.h>

int main(int argc, char *argv[], char *envp[]){
	
	printf("\n I need extra slices of cake!!\n\n\n");
	
	printf(" Argument count: argc -> %d \n\n", argc);
	
	printf(" Arguments: \n");
	for ( int i = 0;argv[i] != '\0'; ++i){
		printf("\t argv[%d] -> %s \n",i, argv[i]);
	}

	printf("\n\n");

}
