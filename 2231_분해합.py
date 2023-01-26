## 브루트포스 알고리즘 : 모든 경우의 수를 확인

from sys import stdin
# stdin = open('input.txt', 'rt')

input = stdin.readline

N =  int(input()) # 분해합을 입력값으로 받음
ans = -1

for i in range(1, N+1): # 해당 분해합의 생성자 찾기
    temp = str(i)
    arr = list(map(int, list(temp))) # i의 각 자리수를 배열에 저장
    res = i + sum(arr) # 분해합 = 생성자 + 각 자리수의 합
    
    if res == N:
        ans = res # ans에 res를 저장한다는 것은 생성자가 존재함을 의미
        break

if ans == -1: # for문을 돌고 나왔을 때 정답을 찾지 못했다면, 생성자가 없는 것이므로
    print(0) # 문제의 조건을 만족하는 0을 출력
else:
    print(i)
