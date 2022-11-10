import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    zero = [1, 0, 1]
    one = [0, 1, 1]

    if n >= 3:
        for i in range(len(zero), n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

    print("{} {}".format(zero[n], one[n]))


# 시간 초과

# import sys
#
# t = int(sys.stdin.readline())
# zero = 0
# one = 0
#
#
# def fibo(n):
#     global zero
#     global one
#
#     if n == 0:
#         zero += 1
#     elif n == 1:
#         one += 1
#     else:
#         fibo(n - 1) + fibo(n - 2)
#
#     return zero, one
#
#
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     zero, one = fibo(n)
#     print("{} {}".format(zero, one))
#     zero = 0
#     one = 0
