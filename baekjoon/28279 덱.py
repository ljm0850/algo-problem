import sys
input = sys.stdin.readline
from collections import deque
def main():
    N = int(input())
    que = deque()
    for _ in range(N):
        order = tuple(map(int,input().split()))
        ord = order[0]
        if ord == 1:
            que.appendleft(order[1])
        elif ord == 2:
            que.append(order[1])
        elif ord == 3:
            if que:
                print(que.popleft())
            else:
                print(-1)
        elif ord == 4:
            if que:
                print(que.pop())
            else:
                print(-1)
        elif ord == 5:
            print(len(que))
        elif ord == 6:
            if que:
                print(0)
            else:
                print(1)
        elif ord == 7:
            if que:
                print(que[0])
            else:
                print(-1)
        elif ord == 8:
            if que:
                print(que[-1])
            else:
                print(-1)

if __name__ == "__main__":
    main()