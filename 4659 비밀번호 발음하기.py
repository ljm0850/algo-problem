def check(target:str)->bool:
    n = len(target)
    for t in target:
        if t in vowel:
            break
    else:
        return False

    for idx in range(n-2):
        if target[idx] in vowel and target[idx+1] in vowel and target[idx+2] in vowel:
            return False
        if not target[idx] in vowel and not target[idx+1] in vowel and not target[idx+2] in vowel:
            return False

    for idx in range(n-1):
        if target[idx] == target[idx+1]:
            if not target[idx] in tVowel:
                return False
    return True

vowel = set(('a','e','i','o','u'))
tVowel = set(('e','o'))
while True:
    target = input()
    if target == 'end':
        break
    ans = check(target)
    if ans:
        print(f'<{target}> is acceptable.')
    else:
        print(f'<{target}> is not acceptable.')