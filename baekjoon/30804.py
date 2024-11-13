def solution(N:int,fruits:list[int])->int:
    if N == 1:
        return 1
    ans = 0
    cnt = [0] * 10
    total = set()
    for i in range(2):
        cnt[fruits[i]] += 1
        total.add(fruits[i])

    s, e = 0, 1
    while s<e:
        if len(total) <= 2:
            ans = max(ans,e-s+1)
            e += 1
            if e == N:
                break
            fruit = fruits[e]
            if cnt[fruit] == 0:
                total.add(fruit)
            cnt[fruit] += 1
        else:
            fruit = fruits[s]
            cnt[fruit] -= 1
            if cnt[fruit] == 0:
                total.remove(fruit)
            s += 1
    return ans

N = int(input())
fruits = list(map(int,input().split()))
ans = solution(N,fruits)
print(ans)