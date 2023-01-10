from sys import stdin
# stdin = open('input.txt', 'rt')
input = stdin.readline

sentence =  input().rstrip()
SS = sentence.upper()
word_lst = list(SS)
word = list(set(SS)) # set() : 중복된 문자 지우기
                     # set으로 변환하고 list로 변환하지 않으면 count() 사용 x

cnt = [] # cnt를 굳이 len을 정해서 만들 필요x

# count() : 문자열 내부에서 특정 문자, 혹은 문자열이 포함되어있는지 계산해서 반환해주는 함수
for i in word:
    cnt.append(word_lst.count(i))

# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우 
if cnt.count(max(cnt)) > 1:
    print('?')
# 가장 많이 사용된 알파벳 대문자로 출력
else:
    print(word[cnt.index(max(cnt))])
