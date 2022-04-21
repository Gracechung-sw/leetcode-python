from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int, n: int) -> int:
        low, high = 1, max(ribbons)
        result = 0
        while low <= high:
            mid = (low + high)//2
            cnt = 0
            for ribbon in ribbons:
                cnt += ribbon // mid
            if cnt >= n:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result


sol = Solution()
print(sol.maxLength([802, 743, 457, 539], 4, 11)) # 200