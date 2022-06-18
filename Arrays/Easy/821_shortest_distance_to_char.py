def shortestToChar(s, c):
    c_indices = [i for i in range(len(s)) if s[i] == c]
    result = []
    for i in range(len(s)):
        min_dist = abs(i-c_indices[0])
        for j in c_indices[1:]:
            if abs(j - i) < min_dist:
                min_dist = abs(j-i)
                # break
        result.append(min_dist)
    return result

s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))