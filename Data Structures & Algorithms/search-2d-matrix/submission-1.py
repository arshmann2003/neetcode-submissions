class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search to find right row of matrix, and then binary search to find the right column
        l1, r1 = 0, len(matrix) - 1
        while l1 <= r1:
            mid = (l1 + r1) // 2
            if target > matrix[mid][-1]:
                l1 = mid + 1
            elif target < matrix[mid][0]:
                r1 = mid - 1
            else: 
                break

        if not (l1 <= r1):
            return False    
    
        mid = (l1 + r1) // 2
        row = matrix[mid]
            
        l2, r2 = 0, len(row) - 1
        while l2 <= r2:
            mid2 = (l2 + r2) // 2
            if target < row[mid2]:
                r2 = mid2 - 1
            elif target > row[mid2]:
                l2 = mid2 + 1
            else:
                return True

        return False



