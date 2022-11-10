# 무작정 주사위 면의 수 중 가장 작은 값 3개를 추출해낸 것이 실수
import sys

n = int(sys.stdin.readline())
die = list(map(int, (sys.stdin.readline().rstrip()).split()))
min_sum = 0


def getMinSum(n, die):
    minimum = 0
    if n == 1:
        die.pop(die.index(max(die)))
        return sum(die)
    else:
        sums = []
        sums.append(min(die[0], die[5]))
        sums.append(min(die[1], die[4]))
        sums.append(min(die[2], die[3]))
        sums = sorted(sums)

        three = 4
        two = 4 + 8 * (n - 2)
        one = 5 * (n - 2) * (n - 2) + 4 * (n - 2)
        sides = [three, two, one]

        for i in range(3):
            minimum += sums[0] * sum(sides)
            sums.pop(sums.index(min(sums)))
            sides.pop()
        return minimum


min_sum = getMinSum(n, die)
print(min_sum)