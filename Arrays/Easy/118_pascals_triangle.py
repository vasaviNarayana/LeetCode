def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    result = [[1]]
    for i in range(numRows):
        temp = [1]
        for j in range(0, len(result[i])-1):
            temp.append(result[i][j]+result[i][j+1])
        temp.append(1)
        result.append(temp)
    return result
print(generate(5))