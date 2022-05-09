from collections import deque
def transnum():
    que = deque()
    que.append(A)
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):               # BFS 깊이를 계산하기 위해 FOR문 사용
            t = que.popleft()
            if t == B:                          # 연산 결과가 B가 될  경우
                return cnt
            if t > B:                           # 가망이 없을 경우
                continue
            que.append(2*t)                     # 2배곱
            que.append(int(str(t)+'1'))         # 오른쪽에 1 추가
    return -1                                   # while que에서 빠져 나온 결과이므로 도달 할 수 없을 경우

A,B = map(int,input().split())
print(transnum())