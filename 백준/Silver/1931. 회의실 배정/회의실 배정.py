import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for i in range(n):
    a, b = map(int, input().split())
    meetings.append((a, b))

meetings.sort(key=lambda x: (x[1], x[0]))  # 종료 시간으로 먼저 정렬, 종료 시간이 같으면 시작 시간으로 정렬

ans = 1  # 첫 번째 회의는 무조건 선택
end_time = meetings[0][1]

for i in range(1, n):
    if meetings[i][0] >= end_time:
        ans += 1
        end_time = meetings[i][1]

print(ans)

