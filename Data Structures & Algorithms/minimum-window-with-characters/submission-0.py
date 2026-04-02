class Solution:
    def minWindow(self, text: str, word: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: sliding window
        """
        pattern = {}
        for letter in word:
            pattern[letter] = pattern.get(letter, 0) + 1
        
        left = 0
        needed_match = len(pattern)
        window = {}
        shorest_match = len(text) + 1
        shortest_string = ""
        
        for right, letter in enumerate(text):

            if letter in pattern:
                window[letter] = window.get(letter, 0) + 1
                if window[letter] == pattern[letter]:
                    needed_match -= 1
            
            while needed_match == 0:
                if right - left + 1 < shorest_match:
                    shorest_match = right - left + 1
                    shortest_string = text[left: right + 1]

                left_letter = text[left]
                if left_letter in pattern:
                    if window[left_letter] == pattern[left_letter]:
                        needed_match += 1
                    window[left_letter] -= 1
                left += 1

        return shortest_string if shorest_match != len(text) + 1 else ""