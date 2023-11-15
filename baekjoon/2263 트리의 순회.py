def make_tree(index1,index2):
    stack = [((index1),(index2))]
    while stack:
        in_index,post_index=stack.pop()
        root = postorder[post_index[1]-1]
        tree[root] = []
        if in_index[1]-in_index[0] == 1:
            continue
        i = index[root]
        if in_index[0] != i:
            l_root = postorder[post_index[0]+i-in_index[0]-1]
            stack.append(((in_index[0],i),(post_index[0],post_index[0]+i-in_index[0])))
            tree[root].append(l_root)
        else:
            tree[root].append(0)
        if i+1 != in_index[1]:
            r_root = postorder[post_index[1]-2]
            stack.append(((i+1,in_index[1]),(post_index[0]+i-in_index[0],post_index[1]-1)))
            tree[root].append(r_root)
        else:
            tree[root].append(0)

def preorder(root):
    stack = [root]
    while stack:
        now = stack.pop()
        print(now,end=' ')
        if tree[now]:
            if tree[now][1]:
                stack.append(tree[now][1])
            if tree[now][0]:
                stack.append(tree[now][0])

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
index = {}
for i in range(n):
    index[inorder[i]] = i

start = postorder[-1]
tree = {}
make_tree((0,n),(0,n))
preorder(postorder[-1])