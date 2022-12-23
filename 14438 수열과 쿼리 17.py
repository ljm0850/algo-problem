import sys,math
input = sys.stdin.readline
def makeTree(s,e,idx):
    if s == e:
        tree[idx] = nums[s]
        return tree[idx]
    mid = (s+e)//2
    tree[idx] = min(makeTree(s,mid,2*idx),makeTree(mid+1,e,2*idx+1))
    return tree[idx]

def updateTree(s,e,idx,targetNode,value):
    if s == e:
        tree[idx] = value
        return
    mid = (s+e) // 2
    if targetNode <= mid:
        updateTree(s,mid,2*idx,targetNode,value)
    else:
        updateTree(mid+1,e,2*idx+1,targetNode,value)
    tree[idx] = min(tree[2*idx],tree[2*idx+1])

def findTree(s,e,idx,startRange,endRange):
    if endRange < s or e < startRange:
        return INF
    if startRange <= s and e <= endRange:
        return tree[idx]
    mid = (s+e) // 2
    return min(findTree(s,mid,2*idx,startRange,endRange),findTree(mid+1,e,2*idx+1,startRange,endRange))

N = int(input())
INF = 1000000000
nums = [INF] + list(map(int,input().split()))
treeLength = 1<<(math.ceil(math.log2(N+1))+1)
tree = [INF] * treeLength
makeTree(0,N,1)
M = int(input())
for _ in range(M):
    cmdType,a,b = map(int,input().split())
    if cmdType == 1:
        updateTree(0,N,1,a,b)
    elif cmdType == 2:
        ans = findTree(0,N,1,a,b)
        print(ans)