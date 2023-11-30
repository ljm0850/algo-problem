import sys
sys.stdin=open('GNS_test_input.txt')

# 카운트 배열을 이용하여 풀었습니다
# ZRO ,ONE, ... , NIN의 수를 계산하여 리스트에 개수를 기록
#그 개수만큼 ZRO, ..., NIN 출력
T=int(input())
num_ord = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for _ in range(T):
    tc, arr_len = input().split()
    arr_len=int(arr_len)
    arr = input().split()
    count_num=[0]*10 #수가 0부터 9까지 10가지
    trs_ls = []

    for i in arr:
        for j in range(len(num_ord)):
            if i == num_ord[j] :
                count_num[j] += 1
    for k in range(10):
        trs_ls += [num_ord[k] for _ in range(count_num[k])]
    print(tc)
    print(*trs_ls)