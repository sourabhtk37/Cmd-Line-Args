#include<stdio.h>
#include<unistd.h>

int main(int argc, char *argv[], char *envp[]){
	printf ("\n\n Filename to be executed -> %s", argv[1]);
	
	// Nothing to see here. Show's over.
	argv[0] = argv[1];
	

	//execv -> execute program specified by filename.
	// -> int execve ( const char *filename, char *const argv[], char *const envp[])
	execve ( argv[1], argv, envp);
}
