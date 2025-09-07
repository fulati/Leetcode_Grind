class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:

            k = l + (r - l) // 2

            time = 0

            for i in range(len(piles)):

                time += math.ceil(piles[i] / k)

            if time > h:
                l = k + 1
            elif time <= h:
                r = k - 1
        
        return l