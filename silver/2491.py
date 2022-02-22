N = int(input())            #숫자의 개수
number_ls = list(map(int,input().split()))
high_cnt = low_cnt = max_cnt = high_num = low_num =0

for i in number_ls:
    if high_num <= i :                  #커질때 cnt 계산
        high_cnt +=1
        high_num = i
        if max_cnt < high_cnt:
            max_cnt = high_cnt
    else:
        high_cnt = 1
        high_num = i

    if low_num >= i :                   #작아질때 cnt 계산
        low_cnt +=1
        low_num = i
        if max_cnt < low_cnt:
            max_cnt = low_cnt
    else:
        low_cnt = 1
        low_num = i
print(max_cnt)