# https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/Q

num = int(input())
for m in range(num):
    a, b, c, d, e, f = input()
    if (int(a) + int(b) + int(c)) == (int(d) + int(e) + int(f)):
        print("YES")
    else:
        print("NO")
