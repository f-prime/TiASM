# ABOUT

TiASM (Tiny Assembly) is a tiny assembly like language that I created in order to try and understand how assembly works a little bit better... without writing actual assembly, because as it turns out
it's a pain in the ass to do that. This was just a tool to help me out in my Computer Organization and Architecture class in college.


# Usage

`python tiasm.py <file.s>`

# System Architecture

- 13 Registers
- r11 contains the output of the CMP/AND/OR/XOR operator
- r12 is the program counter
- 2048 memory locations
- Memory locations 0-1024 are the "Video Memory" or "pixels" on the screen that 
  - 32x32
- Memory locations 1025-2048 are "RAM" and just for storing information

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

# Types

`i<integer>` - Integer

`f<decimal>` - Decimal

`d<register>` - Gets the value of the memory address

`p<register>` - Sets the memory address stored in register to some value

`m<memory_address>` - Gets the value stored in the memory address

