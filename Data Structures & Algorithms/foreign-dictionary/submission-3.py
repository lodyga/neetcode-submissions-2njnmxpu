class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        """
        Time complexity: O(V + E)
            V: unique letters count
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array (graph)
            A: multi-source DFS, topological sort
        """
        prereqs = {letter: set() for word in words for letter in word}

        for index in range(len(words) - 1):
            word = words[index]
            next_word = words[index + 1]

            for index, letter in enumerate(word):
                if index == len(next_word):
                    return ""

                next_letter = next_word[index]
                if letter == next_letter:
                    continue

                prereqs[next_letter].add(letter)
                break

        # -1: not visited, 0: visited, 1: in path / detect a cycle
        visited = [-1] * 26

        def dfs(letter):
            index = ord(letter) - ord("a")
            if visited[index] != -1:
                return visited[index]

            visited[index] = 1

            for prereq in prereqs[letter]:
                if dfs(prereq):
                    return True

            alien_dict.append(letter)
            visited[index] = 0
            return 0

        alien_dict = []
        for letter in prereqs:
            if dfs(letter):
                return ""

        return "".join(alien_dict)        