from sys import stdin
# stdin = open('input.txt', 'rt')
input = stdin.readline

x, y, w, h = map(int, input().rstrip().split())
 
z = 0

print(min(x-z, w-x, y-z, h-y))