N, K = map(int, input().split())
temp = 1
for i in range(0, K):
    temp *= N-i 

temp2 = 1
for j in range(K, 0, -1):
    temp2 *= j

ans = temp // temp2
print(ans)