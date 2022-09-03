T= int(input())
def check(n):
    global triangle
    if triangle[n]:
        return triangle[n]
    else:
        triangle[n]=check(n-1)+check(n-5)
        return triangle[n]

for tc in range(1,T+1):
    N = int(input())
    triangle = [0,1,1,1,2,2,3,4,5,7,9]+[0]*100
    print(check(N))
