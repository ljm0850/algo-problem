T = int(input())

for i in range(T):
    N = int(input())
    price = list(map(int,input().split()))
    gain = 0
    high = price[-1]

    for j in reversed(range(N)):
        if high > price[j] :
            gain += (high - price[j])
        else :
            high = price[j]
    print(f'#{i+1} {gain}')


#밑에는 최대값을 갱신하는 형태, 시간이 오래걸려서 폐기됨

# T = int(input())

# def high(x) :
#     best = x[0]
#     for i in x:
#         if best < i:
#             best = i
#     return best

# for i in range(T):
#     N = int(input())
#     price = list(map(int,input().split()))
#     gain = 0
#     maximum = high(price)
#     for j in range(N-1):
        
#         if price[j] < maximum :
#             gain += maximum-price[j]
#         elif price[j] == maximum :
#             maximum = high(price[j+1::])
#     print(f'#{i+1} {gain}')