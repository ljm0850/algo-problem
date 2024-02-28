def main():
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    check = [[-1] * N for _ in range(N)]  # 이동하려는 위치에 말이 있는지 확인용
    position = [[] for _ in range(K)]  # 각 말의 좌표 및 방향
    for i in range(K):
        r, c, d = map(int, input().split())
        check[r - 1][c - 1] = i
        position[i] = [r-1, c-1, d-1]
    ans = solution(N,K,arr,check,position)
    print(ans)
def solution(N,K,arr,check,position):
    dr, dc = (0, 0, -1, 1), (1, -1, 0, 0)
    groupTail = [i for i in range(K)]  # 각 그룹의 앞,뒤 끝 기록용
    groupMember = [set([i]) for i in range(K)]  # 그룹원 몇명인지 확인용

    for cnt in range(1,1001):
        for player in range(K):
            r, c, d = position[player]
            if r == -1:
                continue

            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N) or (arr[nr][nc] == 2):  # 밖으로 나가거나 파란색 칸
                a, b = divmod(d, 2)
                d = 2 * a + (b + 1) % 2
                nr, nc = r + dr[d], c + dc[d]
                position[player][2] = d
                if not (0 <= nr < N and 0 <= nc < N) or (arr[nr][nc] == 2):  # 이동 방향이 모두 막혀 있을 경우
                    position[player][0] = -1
                    continue

            if arr[nr][nc] == 1:  # 붉은색 칸
                beforeTail = groupTail[player]
                groupTail[beforeTail] = player
                groupMember[beforeTail] = groupMember[player]
                position[player][0] = -1
                player = beforeTail

            check[r][c] = -1
            position[player][0] = nr
            position[player][1] = nc
            if check[nr][nc] != -1:  # 이동칸에 다른 사람이 있다면
                player2 = check[nr][nc]
                groupTail[player2] = groupTail[player]
                groupMember[player2].update(groupMember[player])
                for member in groupMember[player]:
                    position[member][0] = -1

                if len(groupMember[player2]) >= 4:
                    return cnt
            else:
                check[nr][nc] = player
    return -1

if __name__ == '__main__':
    main()