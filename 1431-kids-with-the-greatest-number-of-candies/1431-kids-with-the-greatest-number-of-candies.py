class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maxnum = max(candies)

        for a in candies:
            if a + extraCandies >= maxnum:
                res.append(True)
            else:
                res.append(False)

        return res