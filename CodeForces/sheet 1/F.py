# Link of problem : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/F


def score(a, b, c, d):
    timur = a
    lista = sorted([a, b, c, d], reverse=True)
    return lista.index(timur)


num_of_try = int(input())
for i in range(num_of_try):
    a, b, c, d = map(int, input().split())
    print(score(a, b, c, d))
