def solve(arr,n):
    global ans
    t = arr[0][0]
    for ls in arr:
        for p in ls:
            if p != t:
                temp1 = arr[:n//2]
                temp2 = arr[n//2:]
                arr1,arr2,arr3,arr4 = [],[],[],[]
                for i in range(n//2):
                    arr1.append(temp1[i][:n//2])
                    arr2.append(temp1[i][n//2:])
                    arr3.append(temp2[i][:n//2])
                    arr4.append(temp2[i][n//2:])
                n //= 2
                return '('+ solve(arr1,n)+solve(arr2,n)+solve(arr3,n)+solve(arr4,n) + ')'
    return str(t)

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
ans = ''
print(solve(arr,N))