.section .data
christian:
    .long 0
.section .text
.globl _start
_start:
    movl $10, christian
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80