import sys
sys.stdin = open('input (1).txt')

for tc  in range(1,11):

    N,target = input().split()
    secret_ls = []
    for i in target:
        if secret_ls == []:
            secret_ls.append(i)
        else:
            if i == secret_ls[-1]:
                secret_ls.pop()
            else:
                secret_ls.append(i)
    print(f'#{tc}',''.join(secret_ls))