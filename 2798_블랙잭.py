from sys import stdin
stdin = open('input.txt', 'rt')
input = stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
lst = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_num = card[i]+card[j]+card[k]
            if sum_num <= M:
                lst.append(sum_num)
            
print(max(lst))