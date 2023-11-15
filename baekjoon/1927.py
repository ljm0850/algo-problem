import sys

def heap(n,cnt):
    tree[cnt] = n
    while cnt >1:
        if tree[cnt] < tree[cnt//2]:
            tree[cnt//2],tree[cnt] = tree[cnt],tree[cnt//2]
            cnt //=2
        else:
            break

def delete(cnt):
    print(tree[1])
    tree[1],tree[cnt] = tree[cnt],0
    n = 1
    while n<=cnt//2:
        if tree[2*n] and tree[2*n+1]:
            if tree[2*n] < tree[2*n+1]:             #자손중에서 작은거 찾기
                if tree[n]>tree[2*n]:               #자손이 더 작으면 자리 바꾸기
                    tree[2*n],tree[n] = tree[n],tree[2*n]
                    n = 2*n
                    continue
            else:
                if tree[n] > tree[2*n+1]:
                    tree[n],tree[2*n+1] = tree[2*n+1],tree[n]
                    n = 2*n +1
                    continue
        elif tree[2*n]:
            if tree[n] > tree[2*n]:
                tree[n],tree[2*n] = tree[2*n],tree[n]
                n = 2*n
                continue
        break

N = int(sys.stdin.readline())        #100,000 이하
tree = [0] * (N+1)
cnt = 0
for _ in range(N):
    x = int(sys.stdin.readline())    # 2^31 이하
    if x:
        cnt +=1
        heap(x,cnt)
    else:
        if cnt:
            delete(cnt)
            cnt -= 1
        else:
            print(0)