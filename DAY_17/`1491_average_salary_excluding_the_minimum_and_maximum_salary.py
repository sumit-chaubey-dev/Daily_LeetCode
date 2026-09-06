class Solution:
    def average(self, salary: List[int]) -> float:
        for i in [max(salary), min(salary)]:
            if i in salary:
                salary.remove(i)
        n = len(salary)
        ans = sum(salary) / n
        return ans