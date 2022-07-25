M = int(input())
N = int(input())

prime = []
for num in range(M,N+1):
    if num == 1:
        continue
    n = 2
    while n*n <= num:
        if not num % n:
            break
        n += 1
    if n*n > num:
        prime.append(num)
if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)