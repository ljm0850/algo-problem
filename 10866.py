import sys
N = int(sys.stdin.readline())
deque=[]
for _ in range(N):
    command = sys.stdin.readline().split()
    a = command[0]
    if a == 'push_front':
        deque.insert(0,command[1])
    elif a == 'push_back':
        deque.append(command[1])
    elif a == 'pop_front':
        if deque:
            print(deque.pop(0))
        else: print(-1)
    elif a == 'pop_back' :
        if deque:
            print(deque.pop())
        else: print(-1)
    elif a == 'size':
        print(len(deque))
    elif a == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif a == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif a == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)