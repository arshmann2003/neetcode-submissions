import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a heap and keep the number of elements in the heap to only have k at a time
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)    
            
        
        ans = [num for count, num in heap]
        return ans


