# link of problem : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/H


def multiply(num):
    for i in range(1, 11):
        print("{} x {} = {}".format(i, num, (i * num)))


num = int(input())
multiply(num)
