section .text
global leap_year
leap_year:
    ; Arguments:
    ;   rdi: year

    ; Check if divisible by 4
    mov rax, rdi    ; Move year to rax
    xor rdx, rdx    ; Clear rdx
    mov rcx, 4      ; Move 4 to rcx
    idiv rcx        ; Divide rax by rcx

    test rdx, rdx   ; Check if remainder is 0
    jnz .not_leap   ; If not, jump to .not_leap

    ; Check if divisible by 100
    mov rax, rdi    ; Move year to rax
    xor rdx, rdx    ; Clear rdx
    mov rcx, 100    ; Move 100 to rcx
    idiv rcx        ; Divide rax by rcx

    test rdx, rdx   ; Check if remainder is 0
    jz .check_400   ; If so, jump to .check_400
    jmp .is_leap    ; Otherwise, jump to .is_leap

.check_400:
    ; Check if divisible by 400
    mov rax, rdi    ; Move year to rax
    xor rdx, rdx    ; Clear rdx
    mov rcx, 400    ; Move 400 to rcx
    idiv rcx        ; Divide rax by rcx
    
    test rdx, rdx   ; Check if remainder is 0
    jnz .not_leap   ; If not, jump to .not_leap
    jmp .is_leap    ; Otherwise, jump to .is_leap

.is_leap:
    mov rax, 1      ; Set rax to 1
    ret

.not_leap:
    xor rax, rax    ; Clear rax
    ret

%ifidn __OUTPUT_FORMAT__,elf64
section .note.GNU-stack noalloc noexec nowrite progbits
%endif
