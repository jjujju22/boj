# 소수 = 1과 자기 자신으로만 나누어 떨어지는 자연수

from sys import stdin
stdin = open('input.txt', 'rt')
input = stdin.readline

N = int(input())
n = list(map(int, input().split()))

cnt = 0
# 2는 소수니까, 입력 값에서 이미 2가 있으면 cnt += 1
if 2 in n:
    cnt += 1
    
for i in range(N): 
    if n[i] % 2 == 0: # 2를 제외한 짝수는 소수가 x
        cnt += 0
    else: # 홀수
        nn = 0 
        for k in range(3, n[i]+1): # 3부터 입력된 숫자까지
            if n[i] % k == 0: # 나눴을 때, 나누어 떨어지는 숫자가 존재한다면
                nn += 1 # 더하기 1
        # 위의 for문을 다 돌고 나왔을 때, nn == 1 -> 소수! 
        # ** 들여쓰기를 잘 생각할 것!! 
        if nn == 1: # 소수는 1과 본인으로만 나누어 떨어져야 함. 하지만 모든 수는 1로 나누어 떨어지기 때문에
                            # 1을 제외하고 본인으로 나누어 떨어지는 경우 즉, nn == 1 일때
            cnt += 1
            
print(cnt)