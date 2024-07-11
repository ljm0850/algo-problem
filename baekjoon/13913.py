from collections import deque

def path(S:int, dictionary:dict)->str:
    path_list = []
    point = S
    while point != -1:
        path_list.append(str(point))
        point = dictionary[point]
    return ' '.join(reversed(path_list))

def solution(N:int, K:int)->str:
    if N == K:
        return f'0\n{N}'
    max_length = 100001
    record = {N: -1}
    cnt = 0
    que = deque([N])
    while que:
        cnt += 1
        for _ in range(len(que)):
            point = que.popleft()
            for next_point in (point-1, point+1, 2*point):
                if not (0 <= next_point < max_length) or next_point in record:
                    continue
                record[next_point] = point
                que.append(next_point)
                if next_point == K:
                    return f'{cnt}\n{path(next_point, record)}'
    return ""

N, K = map(int, input().split())
ans = solution(N, K)
print(ans)