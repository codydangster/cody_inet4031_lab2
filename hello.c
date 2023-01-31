#include <stdio.h>
	int main() {
		int a = 2;
		int b = 2;
		int c = a + b;
		int i;

		printf("C says: Hello, World!\n");
		printf("%d + %d = %d\n" ,a,b,c);

		char array[][20] = {"User1", "User2", "User3"};
		for (i = 0; i < 3; i++)
        		printf("%s\n", array[i]);
		return 0;		
	}
