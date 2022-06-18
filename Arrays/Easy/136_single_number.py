def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = nums[0]
    for i in range(1, len(nums)):
        ans = ans^nums[i]
    return ans
nums = [4,1,2,1,2]
print(singleNumber(nums))