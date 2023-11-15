T = int(input())
for tc in range(T):
    N = int(input())
    paper1 = set(map(int,input().split()))
    M = int(input())
    paper2 = list(map(int,input().split()))
    for num in paper2:
        if num in paper1:
            print(1)
        else:
            print(0)