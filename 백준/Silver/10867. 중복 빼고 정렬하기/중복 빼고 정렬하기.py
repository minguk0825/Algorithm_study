n = int(input())
num = list(map(int,input().split()))

## 중복 없애주는 set이라는 라이브러리가 있음!!
s_num = sorted(set(num))

for i in s_num:
    print(i,end=' ')
