; Generated x86 assembly code
section .data
section .text
global _start
_start:
    ; Write variable declarations
    ; Declare variable x. with value 10
    mov dword [x.], 10
    ; Exit system call
    mov eax, 1
    xor ebx, ebx
    int 0x80