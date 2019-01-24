/* Sam van den Eijnden
 * Simple swap function to see how it works in assembly
 * January 24, 2018*/
 
#include <stdio.h>

int main(){
	/*variable declerations*/
	int a = 5; /*gets stored in -12(%rpb)*/
	int b = 3; /*gets stored in -8(%rpb)*/
	int swap; /*eventually gets stored in -4(%rpb)*/
	
	/*swap function*/
	swap = a; /*movl -12(%rpb), %eax; movl %eax, -4(%rpb)*/
	a = b; /*movl -8(%rpb), %eax; movl %eax, -12(%rpb)*/
	b = swap; /*movl -4(%rpb), %eax; movl %eax, -12(%rpb)*/
}
