def solve(l):
    k_max = 0
    while k_max*k_max <= l:
        k_max += 1
    k_max -=1

    stay_length = l-k_max*k_max
    cnt = (2*k_max-1) + (stay_length)//k_max
    if stay_length % k_max:
        cnt +=1

    return cnt

T = int(input())
for tc in range(T):
    x,y = map(int,input().split())
    length = y-x
    ans = solve(length)
    print(ans)