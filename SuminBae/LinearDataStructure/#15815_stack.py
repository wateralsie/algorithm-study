import sys

answer = []
exp = list(sys.stdin.readline().rstrip())

for i in exp:
    if i == '+':
        second = answer.pop()
        first = answer.pop()
        answer.append(first + second)
    elif i == '-':
        second = answer.pop()
        first = answer.pop()
        answer.append(first - second)
    elif i == '*':
        second = answer.pop()
        first = answer.pop()
        answer.append(first * second)
    elif i == '/':
        second = answer.pop()
        first = answer.pop()
        answer.append(int(first / second))
    else:
        answer.append(int(i))

print(answer.pop())
