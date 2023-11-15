N= int(input())
solve = []
sol_num = 0 #최대 길이일때 두번쨰 수
max_cnt=0 #최대 횟수
for n in range(1,N+1):
    x = N # 원본 바뀌는거 방지
    y = n
    cnt = 0
    #문제의 식 실행
    while True:
        if x <0 :
            break
        x,y = y,x-y
        cnt += 1
    if cnt >= max_cnt:
        max_cnt = cnt
        sol_num = n

while True:
    if N < 0:
        break
    solve.append(N)
    N,sol_num = sol_num,N-sol_num
print(max_cnt)
print(*solve)