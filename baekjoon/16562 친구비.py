import sys
input = sys.stdin.readline
def unionAB(a:int,b:int)->None:
    global deepth,group
    A = find_root(a)
    B = find_root(b)
    pay = min(payments[A],payments[B])
    if deepth[A] > deepth[B]:
        group[B] = A
        payments[A],payments[B] = pay,0
    elif deepth[B] > deepth[A]:
        group[A] = B
        payments[B],payments[A] = pay,0
    else:
        group[B] = A
        payments[A],payments[B] = pay,0
        deepth[A] += 1

def find_root(node:int)->int:
    if group[node] == node:
        return node
    group[node] = find_root(group[node])
    return group[node]

N,M,k = map(int,input().split())
payments = [0]+list(map(int,input().split()))
group = [num for num in range(N+1)]
deepth = [0]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    unionAB(a,b)
ans = sum(payments)
if ans <= k:
    print(ans)
else:
    print('Oh no')
