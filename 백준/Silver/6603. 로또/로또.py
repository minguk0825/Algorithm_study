import sys
from itertools import combinations

input = sys.stdin.readline

first_case = True

while True:
    num = list(map(int, input().split()))
    if num[0] == 0:
        break
    else:
        if not first_case:
            print()  # 테스트 케이스 사이에 빈 줄 출력
        first_case = False

        n = num[0]
        num.remove(n)
        comb = list(combinations(num, 6))
        for c in comb:
            print(' '.join(map(str, c)))  # 각 조합을 공백과 함께 출력
            
