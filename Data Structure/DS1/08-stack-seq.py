
# initialize variables
stack = []
n = int(input())
j = 1
testcase = [int(input()) for i in range(n)]
result = ''

# put all items in stack until testcase[i] can be popped.
# if tesetcase[i] is greater than stack[-1], it can be popped.
# else if testcase[i] is smaller than stack[-1] the sequence is not valid.
for i in range(n):
    tc = testcase[i]
    if len(stack) == 0:
        while j != tc:
            stack.append(j)
            j += 1
            result += "+"
        stack.pop()
        result += '-'
    else:
        if tc < stack[-1]: print('NO')
        else:
            if tc == stack[-1]: result += '-'
            if tc > stack[-1]:
                while j != tc:
                    j += 1
                    stack.append(j)
                    result += '+'
print(result)
