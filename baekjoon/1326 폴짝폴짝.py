from collections import deque
import sys
input = sys.stdin.readline

def solution(N,arr,s,e):
    if s == e:
        return 0
    record = [-1] * (N)
    record[s-1] = 0
    que = deque([s-1])
    while que:
        point = que.popleft()
        for i in range(point, N, arr[point]):
            if record[i] == -1:
                if i == e-1:
                    return record[point] + 1
                record[i] = record[point] + 1
                que.append(i)
        for i in range(point, -1, -arr[point]):
            if record[i] == -1:
                if i == e-1:
                    return record[point] + 1
                record[i] = record[point] + 1
                que.append(i)
    return -1

N = int(input())
arr = list(map(int,input().split()))
s,e = map(int,input().split())
ans = solution(N,arr,s,e)
print(ans)