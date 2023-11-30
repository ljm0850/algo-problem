#type1
def check(a):                   #a: list
    l = len(a)
    for i in range(l // 2):
        if a[i] != a[l - i - 1]:
            return False
    return True

for _ in range(10):
    tc = input()
    map_list = [list(map(str, input())) for _ in range(100)]
    map_list2 = [[0]*100 for _ in range(100)]               #map_list2: map_list전치
    length = 100                                            #회문 길이

    for i in range(100):
        for j in range(100):
            map_list2[i][j] = map_list[j][i]

    # for i in range(N):
    #     map_list.append(input())
    # for i in range(N):
    #     str_temp = ''
    #     for k in range(N):
    #         str_temp += map_list[k][i]
    #     map_list2.append(str_temp)
    result = 0                          #최종 회문의 길이_초깃값
    for H in range(length, 0, -1):      #H: 회문길이 변화
        if result >= H:                 #아래 반복문에서 result가 결정된 경우, 종료 위함
            break
        for i in range(100):            #행 고정
            if result == H:             #아래 for 반복하면서 결정된 최종 회문의 길이
                break
            for j in range(100 - H + 1):    #정해둔 H의 길이에 맞는 회문 찾기
                if check(map_list[i][j:j + H]) or check(map_list2[i][j:j + H]):
                    result = H              #회문이 확인되었다면 그때의 H가 회문의 길이
                    break

    print(f'#{tc} {result}')


#type2
T= int(input())
ls = [2,3,5,7,11]
for tc in range(1,T+1):
    num=int(input())
    solve=[]
    for i in range(2,num):
        x = num
        if i**2 > num:
            break
        while x % i ==0:
            solve.append(i)
            x //= i
    print(f'#{tc}',end=' ')
    for j in ls:
        print(solve.count(j),end=' ')
    print()