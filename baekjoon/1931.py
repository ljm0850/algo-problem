import sys

N = int(sys.stdin.readline())               # 100,000 이하
booking = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
booking.sort(key=lambda a: (a[1],a[0]))
cnt = 0
now = 0
for i in booking:
    if i[0] >= now:
        now = i[1]
        cnt +=1
print(cnt)