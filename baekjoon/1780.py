import sys

def check(si,sj,n):
    global m_cnt
    global z_cnt
    global p_cnt
    p = arr[si][sj]
    for i in range(si,si+n):
        for j in range(sj,sj+n):
            if arr[i][j] != p:
                for ii in range(3):
                    for jj in range(3):
                        check(si+ii*(n//3),sj+jj*(n//3),n//3)
                return
    if p == -1:
        m_cnt += 1
    elif p == 0:
        z_cnt += 1
    else:
        p_cnt += 1

N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
m_cnt,z_cnt,p_cnt = 0,0,0
check(0,0,N)
print(m_cnt)
print(z_cnt)
print(p_cnt)