class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        graph = [[float("inf")] * len(word2) + 1 for i in range (len(word1)+1)]

        for j in range (len(word2) + 1):
            graph[len(word1)][j] = len(word2) - j
        for i in range (len(word2) + 1):
            graph[len(word2)][i] = len(word1) - i


        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    graph[i][j] = graph[i + 1][j + 1]
                else:
                    graph[i][j] = 1 + min(graph[i + 1][j], graph[i][j + 1], graph[i + 1][j + 1])

        return graph[0][0]