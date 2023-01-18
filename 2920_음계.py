from sys import stdin
stdin = open('input.txt', 'rt')
input = stdin.readline

sentence =  input().rstrip()

# 입력 받은 숫자를 list 형식으로 만들기
lst = []
for i in range(0, len(sentence), 2):
    lst.append(int(sentence[i]))

# 비교할 리스트 만들기 (1~8)
check = list(range(1, 9)) # ascending
sorted_check = sorted(check, reverse=True) # descending

cnt = [0] * len(lst)

# ascending
for i in range(0, len(lst)):
    if check[i] == lst[i]:
        cnt[i] = 1

# descending
for j in range(0, len(lst)):
    if sorted_check[j] == lst[j]:
        cnt[j] = -1

if sum(cnt) == 8:
    print('ascending')
elif sum(cnt) == -8:
    print('descending')
else:
    print('mixed')