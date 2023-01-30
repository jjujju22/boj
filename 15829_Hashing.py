L = int(input())
word = input()

res = 0

M = 1234567891
for i in range(L):
    res += (ord(word[i])-96) * (31**i) % M
    res %= M
print(res)

