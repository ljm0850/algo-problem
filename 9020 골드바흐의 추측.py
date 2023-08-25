import sys
input = sys.stdin.readline

def prime_num_list(N:int)->list[int]:
    check = [True]*(N+1)
    for i in range(2,(N+1)//2):
        if check[i] == False:
            continue
        num = 2*i
        while num <= N:
            check[num] = False
            num += i
    return check

def search(num:int)->tuple[int,int]:
    global prime_nums
    n = num//2
    s,e = n,n
    while True:
        if prime_nums[s] and prime_nums[e]:
            return s,e
        else:
            s -=1
            e += 1

prime_nums = prime_num_list(10000)
T = int(input())
for _ in range(T):
    num = int(input())
    n1,n2 = search(num)
    print(n1,n2)
