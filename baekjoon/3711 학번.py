def solution(ls:list[int])->int:
    value = 1
    while True:
        temp = set()
        for st in ls:
            now = st % value
            if now in temp:
                break
            temp.add(now)
        else:
            return value
        value += 1

N = int(input())
for tc in range(N):
    G = int(input())
    total = [int(input()) for _ in range(G)]
    ans = solution(total)
    print(ans)