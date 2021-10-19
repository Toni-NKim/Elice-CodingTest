class Stack:
    def __init__(self) :
        self.stack = []

    def push(self, v):
        # insert v to the stack(last in first out)
        self.stack.append(v)
        return self.stack
    
    def pop(self):
        return self.stack.pop(-1) if len(self.stack) > 0 else -1

    def size(self):
        return len(self.stack)
    
    def empty(self):
        return 1 if len(self.stack) == 0 else 0

    def top(self):
        return self.stack[-1] if self.empty() == 0 else -1

# n = number of instructions
n = int(input())

for i in range(n):
    s = Stack()
    # assing instruction, value to variables
    call = input().split()
    if len(call) > 1:
        ins, val = call
        val = int(val)
        method = getattr(s, ins)
        
        if method(val) != None:
            print(method(val))
        
    else:
        ins = call[0]
        method = getattr(s, ins)
        print(method())
