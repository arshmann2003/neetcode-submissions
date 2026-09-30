class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}
        n = len(nums)
        
        for i in range(n):
            num = nums[i]
            complement = target - num

            if complement in seenNums: 
                return [seenNums[complement], i]
            else:
                seenNums[num] = i
