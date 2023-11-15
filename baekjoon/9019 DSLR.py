# n = 초기 숫자,4자리, d1,d2,d3,d4 가 각자리 숫자

# D : n을 2배로, 9999초과시 10000으로 나눈 나머지
# S : n에서 1을 빼기, 음수 될시 9999
# L : 각 자리를 한칸씩 왼쪽으로
# R : n의 각 자리를 오른쪽으로
from collections import deque
dslr = ['D','S','L','R']
def check(A,B):
    que = deque()
    que.append((A,''))
    while que:
        n,cmd = que.popleft()
        if n == B:
            print(cmd)
            return
        dn = [n * 2 % 10000, (n + 9999) % 10000, (n%1000)*10 +n//1000 ,n // 10 + n % 10 * 1000]
        for way in range(4):
            nn = dn[way]
            if not visited[nn]:
                visited[nn] = 1
                que.append((nn,cmd+dslr[way]))

T = int(input())
for tc in range(1,T+1):
    A,B = map(int,input().split())
    visited = [0]*10001
    check(A,B)
