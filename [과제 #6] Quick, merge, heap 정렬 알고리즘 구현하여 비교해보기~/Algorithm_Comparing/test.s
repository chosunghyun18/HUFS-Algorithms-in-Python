	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 15	sdk_version 10, 15, 6
	.globl	_fact                   ## -- Begin function fact
	.p2align	4, 0x90
_fact:                                  ## @fact
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	movq	%rdi, -16(%rbp)
	cmpq	$1, -16(%rbp)
	jge	LBB0_2
## %bb.1:
	movq	$1, -8(%rbp)
	jmp	LBB0_3
LBB0_2:
	movq	-16(%rbp), %rax
	movq	-16(%rbp), %rcx
	subq	$1, %rcx
	movq	%rcx, %rdi
	movq	%rax, -24(%rbp)         ## 8-byte Spill
	callq	_fact
	movq	-24(%rbp), %rcx         ## 8-byte Reload
	imulq	%rax, %rcx
	movq	%rcx, -8(%rbp)
LBB0_3:
	movq	-8(%rbp), %rax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$16, %rsp
	movl	$4, %edi
	callq	_fact
	leaq	L_.str(%rip), %rdi
	movq	%rax, %rsi
	movb	$0, %al
	callq	_printf
	xorl	%ecx, %ecx
	movl	%eax, -4(%rbp)          ## 4-byte Spill
	movl	%ecx, %eax
	addq	$16, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"%lld"


.subsections_via_symbols
