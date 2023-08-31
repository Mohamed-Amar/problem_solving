# link of problems : https://codeforces.com/group/ZzHCrKVEj7/contest/429375/problem/G


def num_of_ones(Petya, Vasya, Tonya):
    if (Petya + Vasya + Tonya) > 1:
        return 1


sure = 0
num_of_ques = int(input())
for i in range(num_of_ques):
    Petya, Vasya, Tonya = map(int, input().split())
    if num_of_ones(Petya, Vasya, Tonya) == 1:
        sure += 1
print(sure)
