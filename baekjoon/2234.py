# 1:서, 2:북, 4:동, 8:남 => 0:남, 1: 동, 2:북, 3:서
def solution(C:int,R:int,arr:list[list[int]])->str:
    check = [[0]*C for _ in range(R)]
    dr,dc = (1,0,-1,0),(0,1,0,-1)
    roomSize = dict()
    neighbor = dict()
    roomNum = 1
    for row in range(R):
        for col in range(C):
            if check[row][col]: continue
            check[row][col] = roomNum
            ls = [(row,col)]
            cnt = 0
            while ls:
                cnt += 1
                r,c = ls.pop()
                wall = bin(arr[r][c])[2:]
                wall = '0'*(4-len(wall))+wall
                for d in range(4):
                    nr,nc = r+dr[d],c+dc[d]
                    if not (0<=nr<R and 0<=nc<C):continue
                    if wall[d] == '1':
                        neighbor[check[nr][nc]] = neighbor.get(check[nr][nc],set())|set([roomNum])
                        continue
                    if check[nr][nc]: continue
                    check[nr][nc] = roomNum
                    ls.append((nr,nc))
            roomSize[roomNum] = cnt
            roomNum += 1
    biggestRoom = 0
    for value in roomSize.values():
        biggestRoom = max(biggestRoom,value)
    
    bestValue = 0
    for i in range(1,roomNum):
        if not neighbor.get(i): continue
        for j in neighbor[i]:
            if i == j: continue
            bestValue = max(bestValue,roomSize[i]+roomSize[j])

    ans = str(roomNum-1) + '\n' + str(biggestRoom) + '\n' + str(bestValue)
    return ans

C,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
ans = solution(C,R,arr)
print(ans)