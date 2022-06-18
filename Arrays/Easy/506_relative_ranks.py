def findRelativeRanks(score):
    """
    :type score: List[int]
    :rtype: List[str]
    """
    scores_arranged = sorted(score, reverse=True)
    ranks_mapped = {}
    result = []
    for i in range(len(scores_arranged)):
        if i == 0:
            ranks_mapped[scores_arranged[0]] = "Gold Medal"
            continue
        if i == 1:
            ranks_mapped[scores_arranged[1]] = "Silver Medal"
            continue
        if i == 2:
            ranks_mapped[scores_arranged[2]] = "Bronze Medal"
            continue
        ranks_mapped[scores_arranged[i]] = str(i+1)
    for j in score:
        result.append(ranks_mapped[j])
    return result

score = [10,3,8,9,4]
print(findRelativeRanks(score))