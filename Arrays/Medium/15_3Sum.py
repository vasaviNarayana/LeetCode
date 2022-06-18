def threeSum(nums):
    result = []
    for i in range(len(nums)):
        temp = []
        for j in range(i+1, len(nums)):
            temp = [(nums[i],nums[j],num) for num in nums[j+1:] if nums[i]+nums[j]+num == 0 and (nums[i],nums[j],num) not in result and (nums[j],nums[i],num) not in result and (nums,nums[j],num[i]) not in result]
            print(temp)
            if len(temp) != 0:
                result += temp
    return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))