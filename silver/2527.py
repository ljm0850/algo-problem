for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
    solve='a'

    if (p1 < x2) or (p2<x1) or (q1< y2) or (q2<y1):
        solve='d'
    elif x1 == p2 or x2== p1:
        if (y1 == q2) or (y2 == q1):
            solve = 'c'
        else:
            solve = 'b'
    elif y1 == q2 or y2 == q1:
        if (x1 == p2) or (x2 == p1):
            solve = 'c'
        else:
            solve = 'b'
    print(solve)