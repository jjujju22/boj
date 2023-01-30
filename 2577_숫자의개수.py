## 내가 푼 방법
lst = []
result = 1

for i in range(3):
    lst.append(int(input()))
    result *= lst[i]

cnt = [0] * 10

for i in str(result):
    cnt[int(i)] += 1

for j in cnt:
    print(j)

## count 함수 이용해서 해보기
lst = []
result = 1

for _ in range(3):
    i = int(input())
    result *= i

result_str = str(result)

cnt = []
for num in range(10):
    cnt = result_str.count(str(num))
    print(cnt)