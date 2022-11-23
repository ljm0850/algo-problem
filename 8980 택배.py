import sys


def solve(N: int, C: int, boxex: list):
    ans = 0
    truck = [0]*(N+1)
    total = 0
    last_check_position = 0

    for box in boxes:
        # 택배 하차
        start, end, value = box
        for position in range(last_check_position, start+1):
            ans += truck[position]
            total -= truck[position]
            truck[position] = 0
        last_check_position = start+1
        # 택배 승차

        # 여유 있으면 바로 태움
        if total + value <= C:
            truck[end] += value
            total += value
        # 중량이 오버 된 경우
        else:
            # 일단 넣을수 있는 만큼 넣음
            truck[end] += C-total
            value -= C-total
            total = C
            # 뒤에서 부터 체크
            for position in range(end+1, N+1)[::-1]:
                # 뒤에 있는 짐 빼기
                if truck[position]:
                    remainbox = max(value - truck[position], 0)
                    # 여기 칸만 비우면 되네
                    if remainbox == 0:
                        truck[position] -= value
                        truck[end] += value
                        break
                    # 더 비워야 되네
                    else:
                        truck[end] += truck[position]
                        value -= truck[position]
                        truck[position] = 0
    # 남은 박스 처리
    for position in range(last_check_position, N+1):
        ans += truck[position]
    return ans


N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
boxes = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
boxes.sort()
answer = solve(N, C, boxes)
print(answer)
