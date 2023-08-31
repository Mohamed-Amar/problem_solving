## link of problem : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/D


def cross(l1, r1, l2, r2):
    if r1 < l2 or l1 > r2:
        return [-1]
    intersection_start = max(l1, l2)
    intersection_end = min(r1, r2)
    return intersection_start, intersection_end


l1, r1, l2, r2 = map(int, input().split())
print(*cross(l1, r1, l2, r2))
