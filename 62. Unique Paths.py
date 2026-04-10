class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        sp = [[1]*n] + [[0]*n for i in range(m-1)]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    sp[i][j] = 1
                else:
                    sp[i][j] = sp[i-1][j]+sp[i][j-1]
        return sp[-1][-1]