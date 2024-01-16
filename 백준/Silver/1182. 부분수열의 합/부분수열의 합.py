import sys
input = sys.stdin.readline
from itertools import combinations

a,b = map(int,input().split())

num = list(map(int,input().split()))
cnt = 0

for i in range(1,a+1):
    comb = combinations(num,i)
    
    for x in comb:
        if sum(x) == b:
            cnt+=1
print(cnt)