class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            coins_used = mid * (mid + 1) // 2
            if coins_used == n:
                return mid
            elif coins_used < n:
                left = mid + 1
            else:
                right = mid - 1
        return right
