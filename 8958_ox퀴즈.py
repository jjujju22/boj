N = int(input())

# 입력시 바로 문제의 점수 출력하도록
for i in range(N):
    a = input()
    score = 0 # O를 확인했을 때의 점수
    sum = 0 # 전체 점수
    for j in a:
        if j == 'O':
            # O을 연속으로 만나면 +1 해줘야하니까
            score += 1
        else:
            score = 0
        sum += score
    print(sum)