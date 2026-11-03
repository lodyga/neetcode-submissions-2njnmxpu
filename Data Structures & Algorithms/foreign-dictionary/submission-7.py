class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        """
        Time complexity: O(V + E)
            V: unique letter count
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: multi-source DFS, topological sort with cycle detection
            Model: graph
        """
        def compare(word1: str, word2: str) -> bool:
            for idx in range(max(len(word1), len(word2))):
                if idx == len(word2):
                    return False  # incorrect
                elif idx == len(word1):
                    return True  # ok
                elif word1[idx] != word2[idx]:
                    prev_letters[word2[idx]].add(word1[idx])
                    break

            return True

        N = len(words)
        prev_letters = {letter: set() for word in words for letter in word}

        for idx in range(N - 2, -1, -1):
            for jdx in range(idx + 1, N):
                if compare(words[idx], words[jdx]) is False:
                    return ""

        def dfs(letter) -> bool:
            idx = ord(letter) - ord('a')

            if visited[idx] != -1:
                return bool(visited[idx])

            visited[idx] = 0

            if letter in prev_letters:
                for prev_letter in prev_letters[letter]:
                    if dfs(prev_letter) is False:
                        return False

            res.append(letter)
            visited[idx] = 1

            return True

        # -1: not visited, 0: visited, 1: in path (detect a cycle)
        visited = [-1] * 26
        res = []

        for letter in prev_letters:
            if dfs(letter) is False:
                return ""

        return "".join(res)
