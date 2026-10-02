class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we can use a binary search in order to find if two indexes exist
        # if the sum of the current two indexes is > target then we move the left index to the right by one. We do the opposite if the sum is < target.
        l, r = 0, len(numbers) - 1
        while l < r: 
            sumIdxs = numbers[l] + numbers[r]
            if sumIdxs < target: 
                l += 1
            elif sumIdxs > target:
                r -= 1
            else:
                return [l+1, r+1]