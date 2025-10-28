def solution():
    N,K = map(int,input().split())  # N : 체스판 크기, K : 말의 개수
    board = [list(map(int,input().split())) for _ in range(N)]  # 체스판 정보
    horses = []  # 말의 정보 (x, y, 방향)
    board_horse = [[[] for _ in range(N)] for __ in range(N)]  # 체스판 위에 쌓인 말의 정보
    for num in range(K):
        r,c,d = map(int,input().split())
        horses.append([r-1,c-1,d-1])  # 0-indexed로 저장
        board_horse[r-1][c-1].append(num)  # 해당 칸에 말 추가

    def isBlueArea(r,c):
        if not (0<=r<N and 0<=c<N) or board[r][c] == 2:
            return True
        return False
    
    def isRedArea(r,c):
        if board[r][c] == 1:
            return True
        return False
    
    # 방향 벡터 (우, 좌, 상, 하)
    dr,dc = (0, 0, -1, 1),(1, -1, 0, 0)
    # 로직
    for turn in range(1,1001):
        for horse in range(K):
            r,c,d = horses[horse]
            nr,nc = r+dr[d],c+dc[d] # nr,nc는 진행 예정인 r,c
            if isBlueArea(nr,nc): # 밖으로 나가거나 파랑색 발판
                match d:
                    case 0: d = 1
                    case 1: d = 0
                    case 2: d = 3
                    case 3: d = 2
                nr,nc = r+dr[d],c+dc[d]
                horses[horse][2] = d
                if isBlueArea(nr,nc):   # 방향을 바꿔도 못가는 경우
                    continue
            idx = board_horse[r][c].index(horse)
            home = board_horse[r][c][:idx]  # 아래 친구들
            away = board_horse[r][c][idx:]  # 자신 + 머리위 친구들
            board_horse[r][c] = home
            if isRedArea(nr,nc):    # 빨간색 발판
                away = away[::-1]
            # 이동 처리
            board_horse[nr][nc].extend(away)
            for obj in away:
                horses[obj][0] = nr
                horses[obj][1] = nc
            if len(board_horse[nr][nc]) >= 4:
                return turn
    return -1

ans = solution()
print(ans)