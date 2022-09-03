import sys
def make_tree():
    tree = {root:[0,0] }
    stack = [root]
    for i in range(1,len(nums)):
        node = nums[i]
        parent = stack[-1]
        if node < parent:
            tree[parent][0] = node
        else:
            while stack and stack[-1]<node:
                parent = stack.pop()
            tree[parent][1] = node
        stack.append(node)
        tree[node] = [0,0]

    return tree

def postorder(node):
    stack = [node]

    while stack:
        parent = stack[-1]
        if tree[parent][0]:
            stack.append(tree[parent][0])
            tree[parent][0] = 0
        elif tree[parent][1]:
            stack.append(tree[parent][1])
            tree[parent][1] = 0
        else:
            print(stack.pop())

nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break
root = nums[0]
tree = make_tree()
postorder(root)