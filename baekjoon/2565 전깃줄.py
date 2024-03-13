def solution(N,arr:list[list[int]])->int:
    arr.sort()
    record = [0]*(501)
    for _,end in arr:
        index = 1
        while True:
            if record[index] == 0 or record[index] >= end:
                record[index] = end
                break
            else:
                index += 1
    for i in range(1,501):
        if not record[i]:
            return N - i + 1
    return 0

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]
ans = solution(N,arr)
print(ans)
