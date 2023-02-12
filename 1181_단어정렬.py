from sys import stdin
stdin = open('input.txt', 'rt')
input = stdin.readline

N = int(input())

word_lst = [[0] * 2 for i in range(N)]
for i in range(N):
    word = input().strip()
    cnt = len(word)
    word_lst[i][0] = cnt    # 문자 글자수 
    word_lst[i][1] = word   # 입력 문자

# 2차원 배열(list) 중복 제거

word_lst = list(set(map(tuple, word_lst))) 
word_lst.sort(key = lambda x : (x[0], x[1]))

for j in range(len(word_lst)):
    print(word_lst[j][1])