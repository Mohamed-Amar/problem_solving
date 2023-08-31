# link of problem : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/O
num = int(input())
char = input()
for i in range(num):
    if (char[i]).isupper():
        print("is upper")
    elif (char[i]).islower():
        print("is lower")
    elif (char[i]).isdigit():
        print("is digit")
    else:
        pass
