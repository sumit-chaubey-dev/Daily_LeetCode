class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1 = 0
        p2 = 0
        for i in range(len(cost)):
            current = min(p1,p2) + cost[i]
            p1 = p2
            p2 = current
        return min(p1,p2)