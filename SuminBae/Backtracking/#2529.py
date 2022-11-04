import sys
from itertools import permutations

n = int(sys.stdin.readline())
# 모든 부등호가 있는 리스트
signs = (sys.stdin.readline().rstrip()).split()
answer = []

for per in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], n + 1):
    count = 0
    for i in range(len(signs)):
        if signs[i] == '<':
            if per[i] < per[i + 1]:
                count += 1
                continue
            else:
                break
        elif signs[i] == '>':
            if per[i] > per[i + 1]:
                count += 1
                continue
            else:
                break
    if count == len(signs):
        answer.append(list(per))

print(*max(answer), sep='')
print(*min(answer), sep='')

