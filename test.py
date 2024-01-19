def twoSum( nums: list[int], target: int) -> list[int]:
    indexes={}
    
    for i in range(len(nums)):
        
        for num in nums:
            # if len(list(set(indexes)))==2:
            #     break
            if num+nums[i]==target:
                indexes.append(nums.index(nums[i]))
                indexes.append(nums.index(num))
                yes=True
                break
        if yes==True:
            break

    print(indexes)
    indexes.sort()


    return list(set(indexes))

print(twoSum([3,2,4],6))

