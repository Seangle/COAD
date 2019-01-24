/* Sam van den Eijnden
 * x86 Assembly generated from swap.c
 * using "gcc swap.c -S -o swap.S"
 * Added comments of what I think it is doing.
 * January 24, 2018
 */
	.file	"swap.c"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	#adds room to stack for program
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	
	#move int 5 into the register associated with 'a'
	movl	$5, -12(%rbp)
	
	#move int 3 into the register associated with 'b'
	movl	$3, -8(%rbp)
	
	#temp not given a value, so it gets ignored until it is used.
	
	#place value of 'a' into 'temp'
	movl	-12(%rbp), %eax
	movl	%eax, -4(%rbp)
	
	#place value of 'b' into 'a'
	movl	-8(%rbp), %eax
	movl	%eax, -12(%rbp)
	
	#place value of 'temp' into 'a'
	movl	-4(%rbp), %eax
	movl	%eax, -8(%rbp)
	
	#swap complete
	
	#remove program from stack
	movl	$0, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.3.0-27ubuntu1~18.04) 7.3.0"
	.section	.note.GNU-stack,"",@progbits
