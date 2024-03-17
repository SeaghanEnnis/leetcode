class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0 for b in range(n+1)]
        ways[0],ways[1] = 1,1

        for x in range(2, n+1):
            ways[x] = ways[x - 1] + ways[x - 2]

        return ways[n]