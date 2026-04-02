class Solution:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    """

    def encode(self, word_list: list[str]) -> str:
        return "".join(str(len(word)) + "#" + word
                       for word in word_list)

    def decode(self, text: str) -> list[str]:
        word_list = []
        index = 0

        while index < len(text):
            word_length = 0
            while text[index].isdigit():
                word_length = 10*word_length + int(text[index])
                index += 1
            
            if text[index] == "#":
                index += 1

            word_list.append(text[index: index + word_length])
            index += word_length

        return word_list