B = int(input()) #스위치 수
switch = list(map(int,input().split())) #스위치 상태
student = int(input()) #100이하 양의정수

for _ in range(student):
    gender,number = map(int,input().split())
    #남학생
    if gender == 1:
        num = number
        while num <= B:
            if switch[num-1] == 0:
                switch[num-1] = 1
            else:
                switch[num-1] = 0
            num += number
    #여학생
    else:
        n = 0
        num = number
        while ((num-1+n) <= B-1) and ((num-1-n) >= 0):
            if switch[num-1+n] == switch[num-1-n]:
                if switch[num-1+n] == 0:
                    switch[num-1+n] = 1
                    switch[num-1-n] = 1
                else:
                    switch[num-1+n] = 0
                    switch[num-1-n] = 0
                n +=1
            else:
                break

for i in range(len(switch)):
    print(switch[i],end=' ')
    if not (i+1) % 20: #출력 형식
        print('')