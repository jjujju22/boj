# 과목 개수
N = int(input())

lst = list(map(int, input().split()))

new = []

for i in range(len(lst)):
    new.append(lst[i]/max(lst)* 100)

total = sum(new)
ave = total/len(lst)
print(ave)