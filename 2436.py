def gcd(a,b): #최대 공약수 구하기
    if b > a :
        a,b = b,a
    while a % b !=0:
        a,b = b, a%b
    return b 

A, B = map(int,input().split())
C= B//A

#C의 공약수 구하기
comdiv = []
for i in range(1,C+1): #zero division
    if i**2 > C : #i가 루트C일 경우문제 발생, 루트 c면 a,b가 같은수라는 소리(a,b는 서로소)
        break
    if C % i == 0:
        comdiv.append([i,C//i])

for j in range(len(comdiv)):
    if gcd(comdiv[j][0],comdiv[j][1]) != 1:
        comdiv[j] = 0

while 0 in comdiv:
    comdiv.remove(0)
print(comdiv[-1][0]*A,comdiv[-1][1]*A)

# --------------------------------------------
# x=최대공약수
# y=최소공배수
# A=x*a
# B=x*B
# y=x*a*b
# a*b = y//x
# a,b는 서로소
