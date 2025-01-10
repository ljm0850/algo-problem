def costCheck(N:int,arr:list[list[int]])->list[tuple[int]]:
    newArr = list()
    for r in range(N):
        for c in range(N):
            num = arr[r][c]
            for nr,nc in ((r+1,c),(r-1,c),(r,c-1),(r,c+1)):
                if not (0<=nr<N and 0<=nc<N):
                    num = -1
                    break
                num += arr[nr][nc]
            if num != -1:
                newArr.append((num,r,c))
    newArr.sort()
    return newArr

def solution(N:int,arr:list[list[int]])->int:
    def isNear(arr1, arr2):
        r1, c1 = arr1[1], arr1[2]
        r2, c2 = arr2[1], arr2[2]
        if abs(r1 - r2) + abs(c1 - c2) <= 2: return True
        return False

    maxCost = 200
    ans = 16*maxCost
    ls = costCheck(N,arr)
    L = len(ls)

    for i in range(L-2):
        for j in range(i+1,L-1):
            if isNear(ls[i],ls[j]): continue
            num = ls[i][0] + ls[j][0]
            if num >= ans:break
            for k in range(j+1,L):
                if isNear(ls[i],ls[k]) or isNear(ls[j],ls[k]):continue
                totalNum = num + ls[k][0]
                if totalNum >= ans:break
                ans = totalNum
    return ans

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = solution(N,arr)
print(ans)