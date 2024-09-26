def solution(password:str,words:list[int])->str:
    for i in range(25):
        new_password = ''
        for alpha in password:
            new_password += chr(97 + (ord(alpha)+i-97)%26)
        for word in words:
            if word in new_password:
                return new_password
    return ''

pw = input()
N = int(input())
words = [input() for _ in range(N)]
ans = solution(pw,words)
print(ans)