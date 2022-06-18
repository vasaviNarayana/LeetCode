def findJudge(trust):
    """
    :type n: int
    :type trust: List[List[int]]
    :rtype: int
    """
    townJudge = trust[0][1]
    for i in range(1, len(trust)):
        if townJudge != trust[i][1]:
            return -1
    return townJudge


n = 3
trust = [[1,3],[2,3]]
print(findJudge(trust))