from sys import stdin
stdin = open('input.txt', 'rt')

input = stdin.readline

T = int(input())

### 풀이 1
# for i in range(T):
#     floor = int(input()) # 층 
#     num = int(input()) # 호 

#     apt = [x for x in range(1, num+1)] # 0층
    
#     for k in range(floor):
#         for j in range(1, num):     
#             apt[j] += apt[j-1]

#     print(apt[-1]) 

### 풀이2
for i in range(T):
    f = int(input()) # 층
    n = int(input()) # 호수
    
    apt = [[x for x in range(1, n+1)] for _ in range(f+1)]

    for j in range(1, f+1):
        for k in range(1, n):
            apt[j][k] = apt[j-1][k] + apt[j][k-1]

    if n == 1:
        print(1)
    else:
        print(apt[j][k])
    