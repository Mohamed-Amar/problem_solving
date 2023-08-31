# Link : https://codeforces.com/group/ZzHCrKVEj7/contest/429848/problem/C
num = int(input())
arr = input().split()
for i in range(num):
    if int(arr[i]) <= 10:
        print(f"A[{i}] = {arr[i]}")
