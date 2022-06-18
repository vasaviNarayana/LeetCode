def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxProfit = 0
    minValue = prices[0]
    for i in range(1, len(prices)):
        minValue = min(prices[i], minValue)
        maxProfit = max(maxProfit, prices[i]-minValue)
    return maxProfit
prices = [7,1,5,3,6,4]
print(maxProfit(prices))