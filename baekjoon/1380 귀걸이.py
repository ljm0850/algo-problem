tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    students = ['']
    for _ in range(N):
        students.append(input())
    total = set()
    for __ in range(2*N-1):
        a,b = input().split()
        if not a in total:
            total.add(a)
        else:
            total.remove(a)
    for p in total:
        print(tc,students[int(p)])