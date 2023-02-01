a, b = map(int, input().split())

# 입력 받은 두 수 중 작은 수 만큼 반복문
if a > b:
    min = b
else:
    min = a

temp = 1
for i in range(min, 1, -1):
    if a % i == 0 and b % i == 0:
        temp = i
        break

print(temp, end='\n')
min_num = a * (b // temp)
print(min_num)