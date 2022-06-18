def findMaxConsecutiveOnes(nums):
    counter = 0 if nums[0] == 0 else 1
    result = 0
    isOne = False if nums[0] == 0 else True
    for i in range(1, len(nums)):
        if nums[i] == 1:
            isOne = True
        if nums[i] == 1 and isOne:
            counter += 1
            isOne = True
            result = max(result, counter)
        else:
            counter = 0
            isOne = False
    return result
nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))