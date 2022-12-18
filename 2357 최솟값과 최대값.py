import sys,math
sys.setrecursionlimit(10**8)
def make_max_tree(s:int,e:int,idx:int)->int:
    global max_tree
    if s == e:
        max_tree[idx] = arr[s]
        return max_tree[idx]
    mid = (s+e) // 2
    a = make_max_tree(s,mid,idx*2)
    b = make_max_tree(mid+1,e,idx*2+1)
    max_tree[idx] = max(a,b)
    return max_tree[idx]

def make_min_tree(s:int,e:int,idx:int)->int:
    global min_tree
    if s == e:
        min_tree[idx] = arr[s]
        return min_tree[idx]
    mid = (s+e) // 2
    a = make_min_tree(s,mid,idx*2)
    b = make_min_tree(mid+1,e,idx*2+1)
    min_tree[idx] = min(a,b)
    return min_tree[idx]

def find_max_min(s:int,e:int,idx:int):
    if e < range_start or s > range_end:
        return (1000000000,0)

    if range_start <= s and e <= range_end:
        return (min_tree[idx],max_tree[idx])
    mid = (s+e)//2
    left = find_max_min(s,mid,idx*2)
    right = find_max_min(mid+1,e,idx*2+1)
    return (min(left[0],right[0]),max(left[1],right[1]))

N,M = map(int,sys.stdin.readline().split())
tree_length = 1<<(math.ceil(math.log2(N)) + 1)
max_tree = [0] * tree_length
min_tree = [0] * tree_length
arr = [int(sys.stdin.readline()) for _ in range(N)]
make_max_tree(0,N-1,1)
make_min_tree(0,N-1,1)

for _ in range(M):
    range_start,range_end = map(int,sys.stdin.readline().split())
    range_start,range_end = range_start-1,range_end-1
    ans = find_max_min(0,N-1,1)
    print(*ans)