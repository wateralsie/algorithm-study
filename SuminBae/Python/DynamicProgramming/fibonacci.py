d = [0] * 100

# 메모이제이션 + 재귀
# 탑다운 방식 (하향식)
def fibo1(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo1(x-1) + fibo1(x-2)
    return d[x]

# 보텀업 방식 (상향식) -> 권장
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]