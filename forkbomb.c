//simple fork bomb to view effects on home machine

#include <stdio.h>

int main(void){
	while(1){
		printf("fork\n");
		fork();
	}
	
}

