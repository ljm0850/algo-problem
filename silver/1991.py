def preorder(start):
    print(chr(start+64),end = '')
    if ch1[start]:
        preorder(ch1[start])
    if ch2[start]:
        preorder(ch2[start])
    return

def inorder(start):
    if ch1[start]:
        inorder(ch1[start])
    print(chr(start+64),end = '')
    if ch2[start]:
        inorder(ch2[start])
    return

def postorder(start):
    if ch1[start]:
        postorder(ch1[start])
    if ch2[start]:
        postorder(ch2[start])
    print(chr(start+64),end = '')
    return

N = int(input())        # 노드의 개수
ch1 = [0] * 30
ch2 = [0] * 30
# ord('A') = 65
for i in range(N):
    temp = list(input().split())
    for j in range(1,3):
        if temp[j] == '.':
            continue
        if j == 1:
            ch1[ord(temp[0])-64] = ord(temp[j])-64
        else:
            ch2[ord(temp[0])-64] = ord(temp[j])-64
preorder(1)
print()
inorder(1)
print()
postorder(1)
print()