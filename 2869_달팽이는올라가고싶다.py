from sys import stdin
# stdin = open('input.txt', 'rt')
input = stdin.readline

A, B, V = map(int, input().split())

# x = 달팽이가 올라가는 일 수
# 정상에 올라간 후에는 미끄러지지 x 때문에 올라ㄲ간 일 수가 미끄러진 일수 보다 하루 많다
# Ax - B(x-1) = V
x = (V-B) / (A-B)
if x == int(x):
    print(int(x))
else:
    print(int(x)+1)