# link of problem : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/C


def getDivision(raiting):
    if raiting >= 1900:
        return 1
    elif raiting >= 1600 and raiting < 1900:
        return 2
    elif raiting >= 1400 and raiting < 1600:
        return 3
    elif raiting < 1400:
        return 4


num = int(input())
for i in range(num):
    f = int(input())
    Division = getDivision(f)
    print("Division ", Division)
