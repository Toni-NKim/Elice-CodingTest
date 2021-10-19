# int(input()) produces timeout error(시간 초과).
# using sys.stdin.readline() saves time dramatically.
from sys import stdin

# n = number of instructions
n = int(stdin.readline())
stack = []

for i in range(n):
    # assigning instruction, value to variables.
    call = list(stdin.readline().split())
    if len(call) > 1:
        ins, val = call
        if ins == "push": 
            stack.append(val)
    
    # aside from push, all instructions are single-worded.
    else:
        ins = call[0]
        if ins == "pop": 
            # as in return, can combine print on the front of shorthand if statements
            print(stack.pop(-1) if len(stack) != 0 else -1)
        if ins == "size": 
            print(len(stack))
        if ins == "empty":
            print(1 if len(stack) == 0 else 0)
        if ins == "top":
            print(stack[-1] if len(stack) != 0 else -1)

# took 84ms.