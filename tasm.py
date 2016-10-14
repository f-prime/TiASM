from __future__ import print_function
import time
import sys
import os
import pygame

class TASM:
    def __init__(self, instructions):
        self.instructions = filter(None, instructions)
        self.registers = {}
        for x in range(0, 14):
            self.registers["r{}".format(x)] = 0
        self.memory = {}
        for x in range(0,2056):
            self.memory[str(x)] = 0
        self.tokens = {
            "mov":self.mov,
            "cmp":self.cmp,
            "add":self.add,
            "sub":self.sub,
            "mul":self.mul,
            "sub":self.sub,
            "jmp":self.jmp,
            "and":self.and_,
            "or":self.or_,
            "xor":self.xor,
            "mod":self.mod,
        }
        pygame.init()

    def cycle(self):
        while self.registers['r12'] < len(self.instructions):
            instruction = self.instructions[self.registers['r12']].lower()
            if instruction[0] == ';':
                self.registers['r12'] += 1
                continue
            instruction = instruction.split()
            if instruction:
                if instruction[0][:3] not in self.tokens:
                    sys.exit("Invalid Instruction: {}".format(instruction[0]))
                else:
                    if instruction[0].endswith("eq"):
                        if self.registers['r11']:
                            self.tokens[instruction[0][:3]](instruction)
                    elif instruction[0].endswith("ne"):
                        if not self.registers['r11']:
                            self.tokens[instruction[0][:3]](instruction)
                    else:
                        self.tokens[instruction[0][:3]](instruction)    
            else:
                self.registers['r12'] += 1
                continue
            self.__formScreen()
            self.registers['r12'] += 1
            time.sleep(0.01)
        if '-r' in sys.argv:
            __import__("pprint").pprint(self.registers)
        if "-m" in sys.argv:
            __import__("pprint").pprint(self.memory)
    def __formScreen(self):
        print("\n" * 80)
        screen = []
        row = []
        for r in range(1025):
            row.append(self.memory[str(r)])
            if len(row) == 32:
                screen.append(row)
                row = []
        for s in screen:
            for t in s:
                print(chr(int(t)), end='')
            print()
    def __resolveValue(self, value):
        if value[0] == 'd':
            return self.memory[str(self.registers[value[1:]])]
        elif value[0] == 'i':
            return int(value[1:])
        elif value[0] == 'r':
            return self.registers[value]
        elif value[0] == 'f':
            return float(value[1:])
        elif value[0] == 'm':
            return self.memory[value[1:]]
    
    def mod(self, instruction):
        location = instruction[1]
        v1 = self.__resolveValue(instruction[2])
        v2 = self.__resolveValue(instruction[3])
        if location[0] == 'r':
            self.registers[location] = v1 % v2
        elif location[0] == 'p':
            self.memory[str(self.registers[location[1:]])] = v1 % v2
        elif location[0] == 'm':
            self.memory[location[1:]] = v1 % v2

    def mov(self, instruction):
        location = instruction[1]
        value = instruction[2]
        if location[0] == 'r':
            self.registers[location] = self.__resolveValue(value)
        elif location[0] == 'p':
            self.memory[str(self.registers[location[1:]])] = self.__resolveValue(value)
        elif location[0] == 'm':
            self.memory[location[1:]] = self.__resolveValue(value)
     
    def cmp(self, instruction):
        left = self.__resolveValue(instruction[1])
        right = self.__resolveValue(instruction[2])
        if left == right:
            self.registers['r11'] = 1
        else:
            self.registers['r11'] = 0

    def add(self, instruction):
        location = instruction[1]
        v1 = self.__resolveValue(instruction[2])
        v2 = self.__resolveValue(instruction[3])
        if location[0] == 'r':
            self.registers[location] = v1 + v2
        elif location[0] == 'p':
            self.memory[str(self.registers[location[1:]])] = v1 + v2
        elif location[0] == 'm':
            self.memory[location[1:]] = v1 + v2
            
    def sub(self, instruction):
        location = instruction[1]
        v1 = self.__resolveValue(instruction[2])
        v2 = self.__resolveValue(instruction[3])
        if location[0] == 'r':
            self.registers[location] = v1 - v2
        elif location[0] == 'p':
            self.memory[str(self.registers[location[1:]])] = v1 - v2
        elif location[0] == 'm':
            self.memory[location[1:]] = v1 - v2
    def mul(self, instruction):
        location = instruction[1]
        v1 = self.__resolveValue(instruction[2])
        v2 = self.__resolveValue(instruction[3])
        if location[0] == 'r':
            self.registers[location] = v1 * v2
        elif location[0] == 'p':
            self.memory[str(self.registers[location[1:]])] = v1 * v2
        elif location[0] == 'm':
            self.memory[location[1:]] = v1 * v2
    def div(self, instruction):
        location = instruction[1]
        v1 = self.__resolveValue(instruction[2])
        v2 = self.__resolveValue(instruction[3])
        if location[0] == 'r':
            self.registers[location] = v1 / v2
        elif location[0] == 'p':
            self.memory[str(self.registers[location[1:]])] = v1 / v2
        elif location[0] == 'm':
            self.memory[location[1:]] = v1 / v2

    def jmp(self, instruction):
        location = self.__resolveValue(instruction[1])
        self.registers['r12'] = location - 1

    def and_(self, instruction):
        left = self.__resolveValue(instruction[1])
        right = self.__resolveValue(instruction[2])
        if left == right:
            self.registers['r11'] = 1
        else:
            self.registers['r11'] = 0
    def or_(self, instruction):
        left = self.__resolveValue(instruction[1])
        right = self.__resolveValue(instruction[2])
        if left or right:
            self.registers['r11'] = 1
        else:
            self.registers['r11'] = 0
    def xor(self, instruction):
        left = self.__resolveValue(instruction[1])
        right = self.__resolveValue(instruction[2])
        if left or right and not (left and right):
            self.registers['r11'] = 1
        else:
            self.registers['r11'] = 0

def main(file_name):
    with open(file_name) as f:
        instructions = []
        for q in f.readlines():
            if len(q) == 0 or q.startswith(";"):
                continue
            instructions.append(q)
        TASM(instructions).cycle()    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python tasm.py <file.s>")
    main(sys.argv[1])
