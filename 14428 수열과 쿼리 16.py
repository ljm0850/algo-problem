import sys,math
input = sys.stdin.readline
def makeTree(s,e,idx):
    if s == e:
        tree[idx] = [nums[s],s]
        return tree[idx]
    mid = (s+e)//2
    left,right = makeTree(s,mid,2*idx),makeTree(mid+1,e,2*idx+1)
    if left[0] <= right[0]: tree[idx] = left
    else: tree[idx] = right
    return tree[idx]

def updateTree(s,e,idx,targetNode,value):
    if s == e:
        tree[idx][0] = value
        return
    mid = (s+e) // 2
    if targetNode <= mid:
        updateTree(s,mid,2*idx,targetNode,value)
    else:
        updateTree(mid+1,e,2*idx+1,targetNode,value)
    left,right = tree[2*idx],tree[2*idx+1]
    if left[0] <= right[0]:tree[idx] = left
    else:tree[idx] = right

def findTree(s,e,idx,startRange,endRange):
    if endRange < s or e < startRange:
        return [INF,0]
    if startRange <= s and e <= endRange:
        return tree[idx]
    mid = (s+e) // 2
    left = findTree(s,mid,2*idx,startRange,endRange)
    right = findTree(mid+1,e,2*idx+1,startRange,endRange)
    if left[0] <= right[0]:
        return left
    else:
        return right

N = int(input())
INF = 1000000001
nums = [INF] + list(map(int,input().split()))
treeLength = 1<<(math.ceil(math.log2(N+1))+1)
tree = [[INF,0] for _ in range(treeLength)]
makeTree(0,N,1)
M = int(input())
for _ in range(M):
    cmdType,a,b = map(int,input().split())
    if cmdType == 1:
        updateTree(0,N,1,a,b)
    elif cmdType == 2:
        ans = findTree(0,N,1,a,b)[1]
        print(ans)