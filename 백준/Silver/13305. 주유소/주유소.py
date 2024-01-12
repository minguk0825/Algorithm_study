import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int,input().split()))
price = list(map(int,input().split()))


p_m = 10000
total = 0
for i in range(n-1):
    p_m = min(price[i],p_m)
    total += p_m * dis[i]
    
print(total)