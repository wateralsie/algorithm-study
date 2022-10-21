import sys

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    request = sys.stdin.readline().split()
    command = request[0]

    if command == "push":
        stack.append(request[1])
    elif command == "pop":
        print(-1 if len(stack) == 0 else stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command == "top":
        print(-1 if len(stack) == 0 else stack[-1])