T = int(input())

for tc in range(T):
    k = int(input())        #층
    n = int(input())        #호
    apart = [_ for _ in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            apart[j] += apart[j-1]
    print(apart[-1])