T= int(input())

for tc in range(1,T+1):
    N,S = map(int,input().split())              # N= 문서의 개수, S = S번째 문서가 언제 출력되는지 파악
    ip = list(map(int,input().split()))
    cnt = 0
    bp = 0                                      #break point
    while bp == 0:
        max_ip = 0
        temp = []
        for i in ip:            #최대값 찾기, 복사
            temp.append(i)
            if i > max_ip:
                max_ip = i

        for i in range(N):
            if ip[i] == max_ip:
                cnt += 1
                temp[i] = -1
                max_ip = max(temp)  #귀찮아서 max
                if i == S:
                    bp = 1
                    break
        ip = temp
    print(cnt)