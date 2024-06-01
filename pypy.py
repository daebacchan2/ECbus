
import heapq
hq = []

v, n = map(int, input().split())
maps = [[] for i in range(v + 1)]
degree = [0 for i in range(v + 1)]

for i in range(n):
    a, b = map(int, input().split())
    maps[a].append(b)
    degree[b] += 1
z = []
tf = True
cnt = 0
for i in range(1, len(degree)):
    if degree[i] == 0:
        k = i
        cnt += 1
        heapq.heappush(hq,i)
while hq:
    node = heapq.heappop(hq)
    z.append(node)
    for i in maps[node]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(hq, i)
            cnt += 1
        elif degree[i] < 0:
            tf = False
            break
if cnt != v or not tf:
    print(-1)
else:
    for j in z:
        print(j)

