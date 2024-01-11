import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
a = int(input())
dis = []

## 나무들 사이의 거리를 dis 리스트에 저장
for i in range(n-1):
    num = int(input())
    dis.append(num-a)
    a = num

## 나무들 사이의 거리들 중 최대공약수 찾기
g = dis[0]
for j in range(1,len(dis)):
    g = gcd(g,dis[j])

result = 0
## 거리가 최대공약수가 아니면 심어야할 나무 수 추가
for each in dis:
    result += each // g - 1
print(result)