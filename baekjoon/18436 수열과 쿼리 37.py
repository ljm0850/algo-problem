import sys,math
input = sys.stdin.readline
def makeTree(s,e,idx):
    if s == e:
        tree[idx] = nums[s]
        return tree[idx]
    mid = (s+e) // 2
    tree[idx] = makeTree(s,mid,2*idx) + makeTree(mid+1,e,2*idx+1)
    return tree[idx]

def updateTree(s,e,idx,node,value):
    tree[idx] += value
    if s == e:
        return
    mid = (s+e) // 2
    if node <= mid:
        updateTree(s,mid,2*idx,node,value)
    else:
        updateTree(mid+1,e,2*idx+1,node,value)

def findOddValue(s,e,idx,startRange,endRange):
    if endRange < s or e < startRange:
        return 0
    if startRange <= s and e <= endRange:
        return tree[idx]
    mid = (s+e) // 2
    left = findOddValue(s,mid,2*idx,startRange,endRange)
    right = findOddValue(mid+1,e,2*idx+1,startRange,endRange)
    return left + right

N = int(input())
nums = [0]+list(map(int,input().split()))
for i in range(N+1):
    nums[i] = nums[i] % 2
treeLength = 1<<(math.ceil(math.log2(N+1))+1)
tree = [0]*treeLength
makeTree(0,N,1)
M = int(input())
for _ in range(M):
    a,b,c, = map(int,input().split())
    if a == 1:
        value = c % 2
        if nums[b] != value:
            if value:
                updateTree(0,N,1,b,value)
            else:
                updateTree(0,N,1,b,-1)
            nums[b] = value
    elif a == 2:
        ans = (c-b+1) - findOddValue(0,N,1,b,c)
        print(ans)
    else:
        ans = findOddValue(0,N,1,b,c)
        print(ans)