# N < 10**9 (1,000,000,000) => 10억 => N**2 일 시 굉장히 오래 걸림
# N == 1 => 0 ? 1 ?
# N == 2 => 1
# N == 3 => 2 (1->3, 1->2->3)
# N == 4 => 4 (1->4, 1->3->4, 1->2->3->4, 1->2->4)
# f(N) = f(1) + f(2) + ... + f(N-1)
# N이 2 이상이면 2**(N-2)

def solution(N:int)->int:
    if N == 1: return 0
    MOD = 1000000007
    ans = pow(2,N-2,MOD)
    return ans 

user_input = input()
ans = solution(int(user_input))
print(ans)
