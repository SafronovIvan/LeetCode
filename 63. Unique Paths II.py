class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid[0]) == 1 and len(obstacleGrid)==1:
            return abs(obstacleGrid[0][0]-1)
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    obstacleGrid[0][0] = obstacleGrid[0][0]*-10**10+1
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -10**10
                    continue
                elif i == 0 and j!= 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif j == 0 and i!= 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = max(obstacleGrid[i-1][j], 0) + max(obstacleGrid[i][j-1], 0)
        for i in obstacleGrid:
            print(i)
        return max(obstacleGrid[-1][-1], 0)