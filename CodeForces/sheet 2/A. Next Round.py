# link :https://codeforces.com/group/ZzHCrKVEj7/contest/429848/problem/A

n, k = map(int, input().split())
scores = list(map(int, input().split()))
counter = 0
k_score = scores[k - 1]
for score in scores:
    if score >= k_score and score > 0:
        counter += 1
print(counter)
