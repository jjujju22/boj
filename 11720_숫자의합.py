# from sys import stdin
# stdin = open('input.txt', 'rt')
# input = stdin.readline

# n =  input().rstrip()

# for i in range((int(n))):
#     a = input()
# sum = 0
# print(a)

# from sys import stdin
# stdin = open('input.txt', 'rt')
# input = stdin.readline

# n, s = map(int, input().split())
# print(n, s)

N = int(input())

a = input()
sum = 0 
for i in range(len(a)):
    sum += int(a[i])

print(sum)