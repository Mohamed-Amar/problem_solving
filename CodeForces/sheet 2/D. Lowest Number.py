# Link :https://codeforces.com/group/ZzHCrKVEj7/contest/429848/problem/D
num = int(input())
arr = list(map(int, input().split()))
print(min(arr), arr.index(min(arr)) + 1)
