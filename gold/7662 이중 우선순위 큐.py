import sys,heapq
T = int(input())
for tc in range(1,T+1):
    k = int(input())                #1,000,000 이하
    check = [0]*k
    heap1 = []
    heap2 = []
    for i in range(k):
        t,n = sys.stdin.readline().split()
        n = int(n)
        if  t=='I':
            check[i] = 1
            heapq.heappush(heap1,(n,i))
            heapq.heappush(heap2,(-n,i,n))

        if t =='D' and n == -1:
            while heap1 and not check[heap1[0][1]] :   # 삭제하려는데 이미 삭제된 수이면
                heapq.heappop(heap1)
            if heap1:
                temp = heapq.heappop(heap1)
                check[temp[1]] = 0
        if t == 'D' and n == 1:
            while heap2 and not check[heap2[0][1]]:
                heapq.heappop(heap2)
            if heap2:
                temp = heapq.heappop(heap2)
                check[temp[1]] = 0
    sol1,sol2 = [],[]
    for hp1 in heap1:
        sol1.append(hp1[0])
    for hp2 in heap2:
        sol2.append(hp2[2])
    sol = list(set(sol1)&set(sol2))
    if sol:
        print(max(sol),min(sol))
    else:
        print('EMPTY')