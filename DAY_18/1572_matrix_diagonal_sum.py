class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            r = mat[i][i]
            l = mat[i][len(mat) - 1 - i]
            total += r + l
            if i == len(mat) - 1 - i:
                total -= r
        return total