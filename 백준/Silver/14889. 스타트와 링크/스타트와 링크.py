import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
graph = []
for i in range(n):
    arr = list(map(int,input().split()))
    graph.append(arr)

members = list(range(n)) 
min_value = sys.maxsize 

for r1 in combinations(members, n//2): ## 조합으로 푼 경우 / 백트래킹 방법도 있음
    start, link = 0, 0
    r2 = list(set(members) - set(r1)) 
    for r in combinations(r1, 2): 
        start += graph[r[0]][r[1]]
        start += graph[r[1]][r[0]]
    for r in combinations(r2, 2): 
        link += graph[r[0]][r[1]]
        link += graph[r[1]][r[0]]
    min_value = min(min_value, abs(start-link)) 
print(min_value)