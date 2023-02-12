from sys import stdin
stdin = open('input.txt', 'rt')
input = stdin.readline

K = int(input())
lst = []
for i in range(K):
    n = int(input().rstrip())
    if n > 0:
        lst.append(n)
print(lst)