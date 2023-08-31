# link : "https://codeforces.com/group/ZzHCrKVEj7/contest/429848/problem/B"
num, lost = map(str, input().split())
nums = input().split()
if lost in nums:
    print(nums.index(lost))
else:
    print("Not Found")
