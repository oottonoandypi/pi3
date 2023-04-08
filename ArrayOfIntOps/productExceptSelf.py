def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        countOfZeros = 0
        productWithNoZeros = 1
        
        for num in nums:
            if num==0:
                countOfZeros+=1
            else:
                productWithNoZeros*=num
        
        if countOfZeros>1:
            return res
        
        index=0
        while index<len(nums):
            if nums[index]==0:
                res[index]=int(productWithNoZeros)
            else:
                if countOfZeros==0:
                    res[index]=int(productWithNoZeros/nums[index])
            
            index+=1
            
        return res