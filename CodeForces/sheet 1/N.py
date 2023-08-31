# link of problem : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/N


def wrong_Sub(num):
    if num % 10 == 0:
        return int(num / 10)
    return num - 1


num, num_of_sub = map(int, input().split())
for i in range(num_of_sub):
    num = wrong_Sub(num)
print(num)
