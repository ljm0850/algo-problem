from collections import deque
import sys
input = sys.stdin.readline
K,L = map(int,input().split())
check = {}
que = deque()
for _ in range(L):
    number = input().rstrip()
    check[number] = check.get(number,0)+1
    que.append(number)

while K > 0 and que:
    now = que.popleft()
    if check[now] == 1:
        print(now)
        K -= 1
    else:
        check[now] -= 1