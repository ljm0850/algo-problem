import sys,math
input = sys.stdin.readline
def make_tree(s,e,idx):
    if s == e:
        tree[idx] = nums[s]
        return tree[idx]
    mid = (s+e)//2
    tree[idx] = make_tree(s,mid,2*idx) + make_tree(mid+1,e,2*idx+1)
    return tree[idx]

def find_sum(s,e,idx):
    if start_range > e or s > end_range:
        return 0

    if start_range <= s and e <= end_range:
        return tree[idx]
    mid = (s+e)//2
    left = find_sum(s,mid,2*idx)
    right = find_sum(mid+1,e,2*idx+1)
    return left + right

def change_tree(s,e,idx,gap,change_nums_idx):
    if idx >= tree_length:
        return 0
    tree[idx] += gap
    mid = (s+e)//2
    if change_nums_idx <= mid:
        change_tree(s,mid,2*idx,gap,change_nums_idx)
    else:
        change_tree(mid+1,e,2*idx+1,gap,change_nums_idx)

N,Q = map(int,input().split())
nums = list(map(int,input().split()))
tree_length = 1<<(math.ceil(math.log2(N))+1)
tree = [0]*tree_length
make_tree(0,N-1,1)
for _ in range(Q):
    x,y,a,b = map(int,input().split())
    if x<=y: start_range,end_range = x-1,y-1
    else: start_range,end_range = y-1,x-1
    ans = find_sum(0,N-1,1)
    print(ans)
    gap = b-nums[a-1]
    nums[a-1] = b
    change_tree(0,N-1,1,gap,a-1)