from sys import stdin

n = stdin.readline().rstrip()
cards = sorted(map(int, stdin.readline().rstrip().split()))
m = stdin.readline().rstrip()
numbers = map(int, stdin.readline().rstrip().split())


def binary_search(n, N, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    # 중간점 값이 찾는 값일 때
    if n == N[mid]:
        return N[start:end + 1].count(n)    # 전체 카드에서 n의 개수
    # 중간점 값보다 찾는 값이 작을 때
    elif n < N[mid]:
        return binary_search(n, N, start, mid - 1)   # 왼쪽 탐색
    else:
        return binary_search(n, N, mid + 1, end)     # 오른쪽 탐색


# 숫자 당 카드개수 알아보기 위해 dictionary 사용
result = {}
result_string = ""

for i in cards:
    start = 0
    end = len(cards) - 1
    if i not in result:
        result[i] = binary_search(i, cards, start, end)

# 정수 m이 숫자 카드의 숫자에 있는지 확인하고
for x in numbers:
    # 있으면 개수 출력
    if x in result:
        result_string += (str(result[x]) + " ")
    # 없으면 0
    else:
        result_string += "0 "

print(result_string.rstrip())
