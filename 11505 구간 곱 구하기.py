import sys,math
input = sys.stdin.readline
def make_tree(s:int,e:int,idx:int)->int:
    if s == e:
        tree[idx] = nums[s]
        return tree[idx]
    mid = (s+e)//2
    tree[idx] = (make_tree(s,mid,idx*2) * make_tree(mid+1,e,idx*2+1)) % 1000000007
    return tree[idx]

def change_tree(s:int,e:int,node:int)-> int:
    if node > tree_length:
        return 1
    if 2*node > tree_length:
        tree[node] = c
        return c
    mid = (s+e)//2
    if b <= mid:
        change_tree(s,mid,node*2)
    else:
        change_tree(mid+1,e,node*2+1)
    tree[node] = (tree[2*node] * tree[2*node+1]) % 1000000007
    return tree[node]

def find_tree(s:int,e:int,idx:int)->int:
    if e < b or s > c:
        return 1

    if b <= s and e <= c:
        return tree[idx]
    mid = (s+e)//2
    left = find_tree(s,mid,idx*2)
    right = find_tree(mid+1,e,idx*2+1)
    return (left * right) % 1000000007

N,M,K = map(int,input().split())
nums = list(int(input()) for _ in range(N))
tree_length = 1<<(math.ceil(math.log2(N))+1)
tree = [1]*tree_length
make_tree(0,N-1,1)
for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        change_tree(1,N,1)
    else:
        ans = find_tree(1,N,1)
        print(ans)