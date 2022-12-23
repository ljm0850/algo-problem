import sys,math
input = sys.stdin.readline
def numChange(num):
    if num > 0: return 1
    elif num == 0: return 0
    else: return -1

def makeTree(s,e,idx):
    if s == e:
        tree[idx] = nums[s]
        return
    mid = (s+e) // 2
    makeTree(s,mid,2*idx)
    makeTree(mid+1,e,2*idx+1)
    tree[idx] = tree[2*idx] * tree[2*idx+1]

def updateTree(s,e,idx,node,value):
    if s == e:
        tree[idx] = value
        return tree[idx]
    mid = (s+e) // 2
    if node <= mid:
        updateTree(s,mid,2*idx,node,value)
    else:
        updateTree(mid+1,e,2*idx+1,node,value)
    tree[idx] = tree[2*idx] * tree[2*idx+1]

def findAns(s,e,idx,startRange,endRange):
    if endRange < s or e < startRange:
        return 1
    if startRange <= s and e <= endRange:
        return tree[idx]
    mid = (s+e) //2
    return findAns(s,mid,2*idx,startRange,endRange) * findAns(mid+1,e,2*idx+1,startRange,endRange)

while True:
    try:
        N,K = map(int,input().split())
        nums = [1]+list(map(int,input().split()))
        for i in range(1,N+1):
           nums[i] = numChange(nums[i])
        treeLength = 1<<(math.ceil(math.log2(N+1))+1)
        tree = [1]*treeLength
        makeTree(0,N,1)
        ans = ''
        for _ in range(K):
            cmdType,a,b = input().split()
            a,b = int(a),int(b)
            if cmdType == 'C':
                b = numChange(b)
                if b != nums[a]:
                    updateTree(0,N,1,a,b)
                    nums[a] = b
            else:
                t = findAns(0,N,1,a,b)
                if t >0:ans += '+'
                elif t==0:ans += '0'
                else: ans += '-'
        print(ans)
    except:
        break