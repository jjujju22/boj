from sys import stdin
stdin = open('input.txt', 'rt')
input = stdin.readline

N = int(input())

lst = []
index = [x for x in range(N)] # 들어온 순서에 따라 인덱스 부여
for i in range(N):
    age, name = map(str, input().split())
    lst.append((int(age), name, index[i])) # append할 때, tupple로 -> 연산 속도

lst.sort(key = lambda x : (x[0], x[2])) # 나이, 들어온 순서에 맞춰 정렬

for k in range(N):
    print(lst[k][0], lst[k][1])