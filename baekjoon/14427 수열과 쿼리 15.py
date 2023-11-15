import sys,math
input = sys.stdin.readline
def makeTree(s:int,e:int,idx:int)->list[int,int]:
    if s == e:
        tree[idx] = [nums[s],s]
        return tree[idx]
    mid = (s+e) // 2
    left = makeTree(s,mid,2*idx)
    right = makeTree(mid+1,e,2*idx+1)
    if left[0]<= right[0]:tree[idx] = left
    else:tree[idx] = right
    return tree[idx]

def updateTree(s,e,idx,targetNode,value):
    if idx > treeLength:
        return
    if s == e:
        tree[idx][0] = value
        return
    mid = (s+e) // 2
    if targetNode <= mid:
        updateTree(s,mid,2*idx,targetNode,value)
    else:
        updateTree(mid+1,e,2*idx+1,targetNode,value)
    left,right = tree[2*idx],tree[2*idx+1]
    if left[0] <= right[0]: tree[idx] = left
    else: tree[idx] = right

INF = 1000000001
N = int(input())
nums = [INF]+list(map(int,input().split()))
treeLength = 1<<(math.ceil(math.log2(N+1))+1)
tree = [INF,0]*treeLength
makeTree(0,N,1)
M = int(input())
for _ in range(M):
    cmdType = list(map(int,input().split()))
    if cmdType[0] == 2:
        print(tree[1][1])
    else:
        ans = updateTree(0,N,1,cmdType[1],cmdType[2])