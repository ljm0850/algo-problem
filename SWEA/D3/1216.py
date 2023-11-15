import copy
def palindrome(arr):        #회문 판독
    for i in range(len(arr)):
        if arr[i] != arr[-1-i]:
            return 0
    else:
        return 1
def transpose(ls):          #전치행렬
    ab=ls
    for i in range(len(ls)):
        for j in range(len(ls[0])):
            if i < j:
                ab[i][j],ab[j][i] = ab[j][i], ab[i][j]
    return ab
for _ in range(10):
    tc= input()
    arr=[]
    arr = [list(input()) for _ in range(100)]
    max_cnt = 0
    arr1 = copy.deepcopy(arr)
    arr2 = transpose(arr1)
    for i in range(100):
        if i >= 100-max_cnt:
            break
        for j in range(100):
            tem = max_cnt
            if j >= 100-max_cnt:
                break
            for k in range(tem,101-j)[::-1]:
                if palindrome(arr[i][j:j+k]) :
                    if max_cnt < k:
                        max_cnt = k
                    break
                if palindrome(arr2[i][j:j+k]):
                    if max_cnt < k:
                        max_cnt = k
                    break
    print(f'#{tc} {max_cnt}')