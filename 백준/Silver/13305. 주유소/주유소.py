import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

total = price[0] * dis[0]  # 첫 번째 도시에서 주유하고 출발
min_price = price[0]  # 현재까지의 최소 주유소 가격 초기화

for i in range(1, n-1):
    min_price = min(min_price, price[i])  # 최소 주유소 가격 업데이트
    total += min_price * dis[i]  # 최소 가격으로 주유하여 이동

print(total)
