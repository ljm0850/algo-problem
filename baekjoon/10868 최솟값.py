import sys,math
input = sys.stdin.readline

def make_tree(s:int,e:int,idx:int)->int:
    global tree
    if s == e:
        tree[idx] = nums[s]
        return tree[idx]
    mid = (s+e)//2
    tree[idx] = min(make_tree(s,mid,2*idx),make_tree(mid+1,e,2*idx+1))
    return tree[idx]

def find_range(s:int,e:int,idx:int,a:int,b:int)->int:
    if e < a or s > b:
        return INF
    elif a <= s and e <= b:
        return tree[idx]
    mid = (s + e)//2
    left = find_range(s,mid,2*idx,a,b)
    right = find_range(mid+1,e,2*idx+1,a,b)
    return min(left,right)

N,M = map(int,input().split())
tree_length = 1<<math.ceil(math.log2(N)+1)
INF = 1000000000
tree = [INF] * tree_length
nums = [int(input()) for _ in range(N)]
make_tree(0,N-1,1)
for _ in range(M):
    a,b = map(int,input().split())
    ans = find_range(0,N-1,1,a-1,b-1)
    print(ans)