class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        k = len(nums1) - len(nums2)
        while j <= len(nums2) - 1:
            nums1[k] = nums2[j]
            k += 1
            j += 1
        
        nums1.sort()