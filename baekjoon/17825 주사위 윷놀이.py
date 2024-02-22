def recur(turn,maxTurn,player,totalPoint):
    global dice,root,check,maxPoint
    if turn == maxTurn:
        maxPoint = max(maxPoint,totalPoint)
        return

    cnt = dice[turn]
    for p in range(len(player)):
        if player[p-1] == [0,0]:
            break

        r,c = player[p]
        # 도달 체크
        if r == -1:
            continue
        nr = r
        nc = c + cnt

        # 현제 root에서 벗어나는지 체크
        if nc < len(root[r]):
            getPoint = root[nr][nc]
            # 숏컷 체크
            if nr == 0 and getPoint % 10 == 0:
                nr = getPoint//10
                nc = 0

            # 중복 위치 체크
            if check[nr][nc]:
                player[p] = [nr,nc]
                check[nr][nc] = False   # 이동 위치 이동 불가
                check[r][c] = True  # 기존 위치 이동 가능

                # 다음턴
                recur(turn+1,maxTurn,player,totalPoint+getPoint)
                player[p] = [r,c]
                check[nr][nc] = True
                check[r][c] = False

            else:
                continue

        # 마지막 길로 이동 or 도착
        else:
            # 마지막 길에서 넘겼을 경우
            if nr == 4:
                player[p] = [-1,-1]
                check[r][c] = True
                recur(turn+1,maxTurn,player,totalPoint)
                player[p] = [r,c]
                check[r][c] = False
            else:
                nr = 4
                nc -= len(root[r])
                if r == 0:
                    nc += 3
                # 결국 도착 할 경우
                if nc >= len(root[nr]):
                    player[p] = [-1,-1]
                    check[r][c] = True
                    recur(turn+1,maxTurn,player,totalPoint)
                    player[p] = [r,c]
                    check[r][c] = False

                elif check[nr][nc]:
                    getPoint = root[nr][nc]

                    player[p] = [nr,nc]
                    check[r][c] = True
                    check[nr][nc] = False
                    recur(turn+1,maxTurn,player,totalPoint+getPoint)
                    player[p] = [r,c]
                    check[r][c] = False
                    check[nr][nc] = True

# 10의 배수마다 shortcut
# shortcut에서 중복위치 추가적으로 확인할 장소 25,30,35,40
dice = list(map(int,input().split()))
root = [[2*i for i in range(20)],[10,13,16,19],[20,22,24],[30,28,27,26],[25,30,35,40]]
check = [[True]*20,[True]*4,[True]*3,[True]*4,[True]*4]
player = [[0,0],[0,0],[0,0],[0,0],[-1,-1]]
maxPoint = 0
recur(0,10,player,0)
print(maxPoint)