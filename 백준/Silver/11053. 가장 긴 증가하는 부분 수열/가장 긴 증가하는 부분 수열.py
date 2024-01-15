import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if num[i]>num[j]:
            dp[i] = max(dp[i],dp[j]+1)  ## i 인덱스 까지 가장 긴 수열의 길이가 dp에 저장됨
            
print(max(dp))
