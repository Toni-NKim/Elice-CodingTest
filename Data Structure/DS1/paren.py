from sys import stdin

# initialize variables
n = int(stdin.readline())
result = ""

for i in range(n):
    given_parens = stdin.readline().rstrip()
    cnt = 0
    for p in given_parens:
        cnt += 1 if p == "(" else -1
        if cnt < 0:
            result += 'NO\n'
            break

    else: result += 'YES\n' if cnt == 0 else 'NO\n'

print(result)
# for-else https://book.pythontips.com/en/latest/for_-_else.html