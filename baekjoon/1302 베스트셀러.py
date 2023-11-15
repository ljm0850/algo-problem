N = int(input())
total = {}
for i in range(N):
    temp = input()
    if total.get(temp):
        total[temp] += 1
    else:
        total[temp] = 1
ans = ''
cnt = 0
for item in total.items():
    if item[1] > cnt:
        ans = item[0]
        cnt = item[1]
    elif item[1] == cnt and ans > item[0]:
        ans = item[0]
print(ans)
