import sys

def heap(n):
    while n > 1:
        if heap_ls[n] > heap_ls[n//2]:
            heap_ls[n],heap_ls[n//2] = heap_ls[n//2],heap_ls[n]
            n //= 2
        else:
            return

def delete():
    print(heap_ls[1])
    heap_ls[1],heap_ls[cnt] = heap_ls[cnt],0
    n = 1
    while n <= cnt//2:
        if heap_ls[2*n] and heap_ls[2*n+1]:
            if heap_ls[2*n] >= heap_ls[2*n+1]:
                if heap_ls[2*n] > heap_ls[n]:
                    heap_ls[n],heap_ls[2*n] = heap_ls[2*n],heap_ls[n]
                    n = 2*n
                    continue
            else:
                if heap_ls[2*n+1] > heap_ls[n]:
                    heap_ls[n],heap_ls[2*n+1] = heap_ls[2*n+1],heap_ls[n]
                    n = 2*n+1
                    continue
        elif heap_ls[2*n]:
            if heap_ls[n] < heap_ls[2*n]:
                heap_ls[2*n],heap_ls[n] =heap_ls[n],heap_ls[2*n]
                continue
        break


N = int(input())
heap_ls = [0]* (N+1)
cnt = 0
for _ in range(N):
    i = int(sys.stdin.readline())
    if i:
        cnt +=1
        heap_ls[cnt] = i
        heap(cnt)
    else:
        delete()
        if cnt:
            cnt -= 1