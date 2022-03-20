def transpose(arr,n):
    temp = [[] for _ in range(n)]
    for i in range(n//2):
        for j in range(n):
            temp[j].append(arr[i][j])

    return temp


def paper(arr,n):
    global bcnt
    global wcnt
    t = arr[0][0]
    bp = 0
    for i in range(n):
        if bp:
            break
        for j in range(n):
            if arr[i][j] != t:
                temp1 = transpose(arr[n//2:],n)
                temp2 = transpose(arr[:N//2],n)
                arr1 = temp1[n//2:]
                arr2 = temp1[:n//2]
                arr3 = temp2[n//2:]
                arr4 = temp2[:n//2]
                paper(arr1,n//2)
                paper(arr2,n//2)
                paper(arr3,n//2)
                paper(arr4,n//2)
                bp = 1
                return
    if t :
        bcnt += 1
    else:
        wcnt += 1

wcnt = 0
bcnt = 0
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]            # N = 2**7 이하
paper(arr,N)

print(wcnt)
print(bcnt)