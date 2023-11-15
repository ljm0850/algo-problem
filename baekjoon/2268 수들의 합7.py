# pypy3 코드, python 제출시 시간초과
import sys,math
input = sys.stdin.readline
def updateTree(s,e,idx,value,T):
    if idx >= treeLength:
        return
    if s == e:
        tree[idx] = c
        return
    tree[idx] += value
    mid = (s+e) // 2
    if T <= mid:
        updateTree(s,mid,2*idx,value,T)
    else:
        updateTree(mid+1,e,2*idx+1,value,T)

def findSumArr(s,e,idx):
    if findEnd < s or e < findStart:
        return 0
    if findStart <= s and e <= findEnd:
        return tree[idx]
    mid = (s+e) //2
    left = findSumArr(s,mid,2*idx)
    right = findSumArr(mid+1,e,2*idx+1)
    return left + right

N,M = map(int,input().split())
treeLength = 1<<math.ceil(math.log2(N)+1)
tree = [0]*treeLength
nums = [0]*(N+1)
for _ in range(M):
    a,b,c = map(int,input().split())
    if a == 0:
        if b <= c:
            findStart,findEnd = b-1,c-1
        else:
            findStart,findEnd = c-1,b-1
        ans = findSumArr(0,N-1,1)
        print(ans)
    elif a == 1:
        updateTree(0,N-1,1,c-nums[b],b-1)
        nums[b] = c
