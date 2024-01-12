n = int(input())
dp=[]
dp.append(1) ## dp[0] = 1
dp.append(2) ## dp[1] = 2
if n > 2:
    for i in range(2,n):
        dp.append(dp[i-2]+dp[i-1])

print(dp[n-1] % 10007)

