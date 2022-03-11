n,m,b = map(int,input().split())
arr_cnt = [0]*257

max_h = 0
min_h = 256
for i in range(n):
    temp = list(map(int,input().split()))
    for j in temp:
        if j > max_h:
            max_h = j
        if j < min_h:
            min_h = j
        arr_cnt[j] += 1
h = min_h
min_time=12800000000
for i in range(min_h,max_h+1):  #목표 높이
    temp = b
    time = 0
    for j in range(min_h,max_h+1):  #땅의 높이
        if i < j:              # 목표 높이보다 땅이 높으면
            time += (j-i)*arr_cnt[j]*2
            temp += (j-i)*arr_cnt[j]
        elif i > j:             #목표 높이보다 땅이 낮으면
            time += (i-j)*arr_cnt[j]
            temp -= (i-j)*arr_cnt[j]
    if temp < 0:
        continue
    if min_time >= time:
        min_time = time
        h = i
print(min_time,h)