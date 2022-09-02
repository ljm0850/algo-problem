def make_prime_number(n):
     numbers = [False]*2+[True]*(n-1)
     for num in range(2,n+1):
         if numbers[num]:
             for multiple in range(2*num,n+1,num):
                 numbers[multiple] = False
     prime = []
     for i in range(2,n+1):
        if numbers[i]:
            prime.append(i)
     return prime

def solve(arr,n):
    if not arr:
        return 0
    cnt = 0
    s,e,l = 0,0,len(arr)
    total = arr[0]
    while True:
        if total < n:
            e += 1
            if e < l:
                total += arr[e]
            else:
                return cnt
        elif total > n:
            if s < l:
                total -= arr[s]
                s += 1
            else:
                return cnt
        else:
            cnt += 1
            if s <l:
                total -= arr[s]
                s += 1
            else:
                return cnt

N = int(input())
prime_numbers = make_prime_number(N)
ans = solve(prime_numbers,N)
print(ans)