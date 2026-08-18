class Solution:
    def maximumWealth(self, accounts):
        rich = []
        for i in accounts:
            rich.append(sum(i))
        return max(rich)