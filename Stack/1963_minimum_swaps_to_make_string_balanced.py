def minSwaps(s):
    opened = 0
    for ch in s:
        opened = opened + 1 if ch == "[" else opened - 1 if opened > 0 else opened
    return (opened+1) // 2

s = "]]][][[["
print(minSwaps(s))