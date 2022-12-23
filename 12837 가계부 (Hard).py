import sys,math
input = sys.stdin.readline
def updateTree(s,e,idx,day,value):
    tree[idx] += value
    if s == e:
        return
    mid = (s+e) // 2
    if day <= mid:
        updateTree(s,mid,2*idx,day,value)
    else:
        updateTree(mid+1,e,2*idx+1,day,value)

def sumValue(s,e,idx,startRange,endRange):
    if endRange < s or e < startRange:
        return 0
    if startRange <= s and e <= endRange:
        return tree[idx]
    mid = (s+e) // 2
    return sumValue(s,mid,2*idx,startRange,endRange) + sumValue(mid+1,e,2*idx+1,startRange,endRange)

N,Q = map(int,input().split())
treeLength = 1<<(math.ceil(math.log2(N+1))+1)
tree = [0]*treeLength
for _ in range(Q):
    cmdType,a,b = map(int,input().split())
    if cmdType == 1:
        updateTree(0,N,1,a,b)
    elif cmdType == 2:
        ans = sumValue(0,N,1,a,b)
        print(ans)