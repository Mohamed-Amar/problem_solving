# link of problem : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/E


def Posit(a, b, c):
    if c >= (a + b):
        return (c - (a + b)) + 1
    return 0


a, b, c = sorted(map(int, input().split()))
print(Posit(a, b, c))
