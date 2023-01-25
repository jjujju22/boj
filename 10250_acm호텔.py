from sys import stdin
# stdin = open('input.txt', 'rt')
input = stdin.readline

# Test data 개수
T = int(input().rstrip())

# sol1
for _ in range(T):
    H, W, N = map(int, input().rstrip().split(" "))
    num, floor = (N // H), (N % H)
    if floor == 0:
        floor = H
        print(floor*100 + num)
    else:
        print(floor * 100 + (num+1))


# sol2
# for _ in range(T):
#     H, W, N = map(int, input().rstrip().split())
#     cnt = 0
#     for j in range(W):
#         for i in range(H):
#             cnt += 1
#             temp = (i+1) * 100 + (j+1)

#             if cnt == N:
#                 print(temp)
#                 break


# 2차원 배열 만들기!!
# for _ in range(T):
#     H, W, N = map(int, input().rstrip().split())
    
#     # 2차원 배열을 만들 때는 가로는 곱셈으로 세로는 반복문으로 해야해요~!
#     room = [[0] * W for _ in range(H)]
#     cnt = [[0] * W] * H
#     for j in range(H):
#         for i in range(W):
#             room[j][i] = (100+(i+1)) + (j*100) 
#     print(room)

