# link of problem : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/P
ref = "codeforces"
num = int(input())
for i in range(num):
    char = input()
    for i in range(len(ref)):
        if char == ref[i]:
            print("yes")
            break
    else:
        print("no")
