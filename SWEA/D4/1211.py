import sys
sys.stdin=open('input (1).txt')

def ladder(arr,i,j):
    cnt = 0
    while i > 0:
        if j+1 <= 99 and arr[i][j+1] == '1':
            while j+1 <= 99 and arr[i][j+1] == '1':
                j += 1
                cnt +=1
        elif j-1 >= 0 and arr[i][j-1] == '1':
            while j-1 >= 0 and arr[i][j-1] == '1':
                j -= 1
                cnt +=1
        i -= 1
        cnt +=1
    return cnt,j


for _ in range(10):
    tc = int(input())
    arr = [input().split() for _ in range(100)]
    test = arr
    start_ls=[]
    min_cnt =10000
    min_j = 0
    for i in range(100):
        if arr[99][i] == '1':
            start_ls.append(i)
    for s in start_ls:
        cnt,j=ladder(arr,99,s)
        if cnt  < min_cnt:
            min_cnt = cnt
            min_j = j
    print(f'#{tc} {min_j}')
