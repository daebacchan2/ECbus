from bisect import bisect_left
n = int(input())
li = list(map(int, input().split()))
k = [[0 for i in range(3)] for j in range(n)]
for i in range(n):
    k[i][0] = li[i]
    k[i][1] = i + 1
k.sort(key = lambda x : x[0])
for i in range(1, n):
    if k[i][0] == k[i - 1][0]:
        k[i][2] = k[i - 1][2]
    else:
        k[i][2] = k[i - 1][2] + 1
k.sort(key = lambda x : x[1])
for i in range(n):
    print(k[i][2], end = ' ')