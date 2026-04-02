class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        Time complexity: O(V + E)
            V: unique letters count
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph, topological sort
        """
        # prereqs = {}
        prereqs = {letter: set() for word in words for letter in word}
        for index in range(len(words) - 1):
            word = words[index]
            next_word = words[index + 1]
            
            for j in range(max(len(word), len(next_word))):
                if j == len(word):
                    break
                elif j == len(next_word):
                    return ""
                elif word[j] != next_word[j]:
                    # if next_word[j] not in prereqs:
                    #     prereqs[next_word[j]] = set()
                    prereqs[next_word[j]].add(word[j])
                    break
        
        alien_dict = []
        # None: not visited, False: visited, True: on current patch (detect cycle)
        visited = [None] * 26
        
        def dfs(letter):
            if visited[ord(letter) - ord("a")] is not None:
                return visited[ord(letter) - ord("a")]
            elif letter not in prereqs:
                alien_dict.append(letter)
                return False

            visited[ord(letter) - ord("a")] = True
            
            for prereq in prereqs[letter]:
                if dfs(prereq):
                    return True
            
            alien_dict.append(letter)
            visited[ord(letter) - ord("a")] = False

        for letter in prereqs:
            if dfs(letter):
                return ""

        return "".join(alien_dict)