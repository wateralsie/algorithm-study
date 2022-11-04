import sys

request = (sys.stdin.readline().rstrip()).split()
limit = int(request[0])
size = int(request[1])

sequence = []


def dfs(start):
    if len(sequence) == size:
        print(*sequence)
        return

    for i in range(start, limit + 1):
        if i not in sequence:
            sequence.append(i)
            dfs(i + 1)
            sequence.pop()


dfs(1)
