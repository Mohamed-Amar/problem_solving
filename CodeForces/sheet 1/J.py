## link of problem : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/J

num_of_rows = int(input())
for i in range(num_of_rows):
    nums = sorted(map(int, input().split()))
    if sum([nums[0], nums[1]]) == nums[2]:
        print("YES")
    else:
        print("NO")
