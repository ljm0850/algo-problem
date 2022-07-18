def solve():
    s,e = 0, N-1
    s1,s2 = solution[s],solution[e]

    while s<e:
        ph = solution[s]+solution[e]
        if abs(ph) < abs(s1+s2):
            s1,s2 = solution[s],solution[e]
        if ph <0:
            s += 1
        else:
            e -= 1
    print(s1,s2)

N = int(input())
solution = sorted(list(map(int,input().split())))
solve()
