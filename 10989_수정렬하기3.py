### count 정렬문제!!!
## 모든 숫자를 오른차순, 내림차순을 정렬한다고 할때,,!!
## 가장 빠르게 sorting 할 수 있는 방법
# 메모리,,,ㅎ 샤갈..ㅎ

from sys import stdin
stdin = open('input.txt', 'rt')
input = stdin.readline

N = int(input())

num_lst = [0] * 10001

for i in range(N):
    num = int(input().rstrip())
    num_lst[num] += 1

for k in range(len(num_lst)):
    if num_lst[k] > 0:
        for l in range(num_lst[k]):
            print(k)