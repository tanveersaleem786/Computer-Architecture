"""CPU functionality."""
import sys
# opcodes
LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010
ADD = 0b10100000
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET = 0b00010001

class CPU4:
    """Main CPU class."""
    def __init__(self):
        """Construct a new CPU."""
        # Total memory
        self.ram = [0] * 256
        # General register
        self.reg = [0] * 8
        # Program Counter
        self.pc = 0
        # Store the starting position of stack pointer in register 7.
        self.reg[7] = 0xF4
        self.running = False
        self.instruction_mapping = dict()
        self.instruction_mapping[LDI] = self.ldi
        self.instruction_mapping[PRN] = self.prn
        self.instruction_mapping[HLT] = self.hlt
        self.instruction_mapping[MUL] = self.mul
        self.instruction_mapping[ADD] = self.add
        self.instruction_mapping[PUSH] = self.push
        self.instruction_mapping[POP] = self.pop
        self.instruction_mapping[CALL] = self.call
        self.instruction_mapping[RET] = self.ret
        print()

       
    def load(self, filename):
        """Load a program into memory."""
        address = 0
        # Open file and load in memory
        with open(filename) as file:
            for line in file:
                split_line = line.split("#")
                instruction = split_line[0].strip()
                if instruction != '':
                    self.ram[address] =  int(instruction, 2)
                    address += 1
        # For now, we've just hardcoded a program:
        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]
        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1
    def ram_read(self, mar):
        return self.ram[mar]
    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr
    # Set value in register
    def ldi(self, *params):
        self.reg[params[0]] = params[1]
        # Move pointer to next instruction
        self.pc += 3
    # Print value from register
    def prn(self, *params):
        print(self.reg[params[0]])
        self.pc += 2
    def mul(self, *params):
        self.alu("MUL", params[0], params[1])
        self.pc += 3
    def add(self, *params):
        self.alu("ADD", params[0], params[1])
        self.pc += 3
    def push(self, *params):
        # Decreament in the stack pointer position.
        self.reg[7] -= 1
        # Copy the value of given register into stack.
        self.ram_write(self.reg[7], self.reg[params[0]])
        self.pc += 2
    def pop(self, *params):
        # Copy the value from stack  into given register.
        self.reg[params[0]] = self.ram_read(self.reg[7])
        self.reg[7] += 1
        self.pc += 2
    def call(self, *params):
        # Store the return address (pc + 2) onto the stack
        # Decreament in the stack pointer position.
        self.reg[7] -= 1
        # Write return address
        self.ram_write(self.reg[7], self.pc + 2)
        # Set pc to the value inside the given register
        self.pc = self.reg[params[0]]

        
    def ret(self):
        # Set pc to the value at the top of the stack
        self.pc = self.ram_read(self.reg[7])
        # Pop from stack
        self.reg[7] += 1

    # Exit from program
    def hlt(self, *params):
        self.running = False
        exit(1)
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")
    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """
        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')
        for i in range(8):
            print(" %02X" % self.reg[i], end='')
        print()
    def run(self):
        """Run the CPU."""
        self.running = True
        while self.running:
            # get current instruction and store in memory
            instruction = self.ram_read(self.pc)
            if instruction != RET:
                # store bytes
                operand_a = self.ram_read(self.pc + 1)
                operand_b = self.ram_read(self.pc + 2)
            if instruction in self.instruction_mapping:
                if instruction == RET:
                    self.instruction_mapping[instruction]()
                else:    
                    self.instruction_mapping[instruction](operand_a, operand_b)
            else:
                print(f"Unknown Instruction {instruction} {bin(instruction)}")
                exit(1)