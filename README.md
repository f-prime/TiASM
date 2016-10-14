# ABOUT

TASM (Tiny Assembly) is a tiny assembly like language that I created in order to try and understand how assembly works a little bit better... without writing actual assembly, because as it turns out
it's a pain in the ass to do that. This was just a tool to help me out in my Computer Organization and Architecture class in college.

# System Architecture

- 12 Registers
- r11 contains the output of the CMP/AND/OR/XOR operator
- r12 is the program counter
- r13 is the input register (when a key is pressed the value goes here)
- 1024 memory locations
- Memory locations 0-1024 are the "Video Memory" or "pixels" on the screen that 
  - 32x32
- Memory locations 1025-2056 are "RAM" and just for storing information

# Instructions

- MOV(eq)(ne) <from> <to> [could be memory address or register]
- CMP <p1> <p2> [puts result in r11]
- ADD(eq)(ne) <out> <p1> <p2>
- SUB(eq)(ne) <out> <p1> <p2>
- MUL(eq)(ne) <out> <p1> <p2>
- SUB(eq)(ne) <out> <p1> <p2>
- JMP(eq)(ne) <instruction-number starting from zero>
- AND(eq)(ne) <p1> <p2>
- OR(eq)(ne) <p1> <p2>
- XOR(eq)(ne) <p1> <p2>
- STR(eq)(ne) <regormem> <variable> [stores value from register or memory in varaible]
- LD(eq)(ne) <regormem> <variable> [loads data intro register from variable]

# Types

`i<integer>` - Integer
`f<decimal>` - Decimal
`d<register>` - Gets the value of the memory address
`p<register>` - Sets the memory address stored in register to some value
`m<memory_address>` - Gets the value stored in the memory address

# Hello

mov 0 i72 ;Print the character 'H' to the screen at video memory slot 0
mov 1 i101 ;print the character 'e' to the screen at video memory slot 1
mov r1 i0 ;Move the integer value 0 to the register r1
mov r2 i1 ;Move the integer value 1 to r2
add r2 r2 i1  ;Increment the value  in register r1 by 1 
mov vr2 c108 ;print the character `l` to the screen at the memory address located in the register r2
cmp r2 i3 ; check if the value in register r2 is equal to 3
jmpne 4 ; if it is not jump to the 4th instruction in the list (starting from zero)
mov 4 i111 ; Move the character 'o' to the video memory address 4

