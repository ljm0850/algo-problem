N,r,c = map(int,input().split())        # r행 c열
ans = 0
while N >0:
    N -= 1
    if r < 2**N and c<2**N:
        continue
    elif r < 2**N and c>=2**N:
        ans += 4**N
        c -= 2**N
    elif r >= 2**N and c <2**N:
        ans += 2*4**N
        r -= 2**N
    elif r>= 2**N and c>=2**N:
        ans += 3*4**N
        c -= 2**N
        r -= 2**N
print(ans)