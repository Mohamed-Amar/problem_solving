# link of problem : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/I

sympol = input()  # +
nums = int(input())  # 3
num_of_sympols = input().split()  # [2,3,6]
for i in range(nums):
    print(int(num_of_sympols[i]) * sympol)
