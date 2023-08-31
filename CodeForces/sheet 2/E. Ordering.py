# link : https://codeforces.com/group/ZzHCrKVEj7/contest/429848/problem/E
n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
print(*num_list)
num_list.sort(reverse=True)
print(*num_list)
