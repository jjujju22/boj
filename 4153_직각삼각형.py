from sys import stdin
# stdin = open('input.txt', 'rt')

input = stdin.readline

x, y, z = 1, 1, 1

# while 1 ==> 무한 루프!!
while 1:
    x, y, z = map(int, input().rstrip().split())
    if x == 0 and y==0 and z==0: # input 바로 아래에서 input 조건을 주기
        break

    mn = min(x, y, z) # min은 함수 이름이므로 min말고 다른 이름으로 변수 정의 (mn)
    mx = max(x, y, z) # max도 마찬가지!
    mid = x + y + z - mn - mx

    if mx**2 == mn**2 + mid**2:
        print('right')
    else:
        print('wrong')