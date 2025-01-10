def solution(N:int,arr:list[list[int]])->int:
    def find_M(N:int,arr:list[list[int]]):
        for r in range(N):
            for c in range(N):
                if arr[r][c] == 0:
                    return (r,c)
        return (-1,-1)
    def check(N:int,arr:list[list[int]],position:tuple[int]):
        total = 0
        # row 체크
        for r in range(N):
            sum_value = 0
            if r == position[0]: continue
            for c in range(N):
                sum_value += arr[r][c]
            if total == 0: total = sum_value
            elif total != sum_value: return -1
        # collum 체크
        for c in range(N):
            sum_value = 0
            if c == position[1]: continue
            for r in range(N):
                sum_value += arr[r][c]
            if total != sum_value: return -1
        # M 체크
        sum_value1,sum_value2 = 0,0
        r,c = position
        for i in range(N):
            sum_value1 += arr[r][i]
            sum_value2 += arr[i][c]
        if sum_value1 != sum_value2: return -1
        value = total - sum_value1
        arr[position[0]][position[1]] = value

        # 대각 체크
        sum_value1,sum_value2 = 0,0
        for num in range(N):
            sum_value1 += arr[num][num]
            sum_value2 += arr[num][N-num-1]
        if (total != sum_value1 or total != sum_value2):return -1
        return value
    position = find_M(N,arr)
    return check(N,arr,position)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = solution(N,arr)
print(ans)