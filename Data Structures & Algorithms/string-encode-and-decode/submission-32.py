class Solution:
    """
    Time complexity: O(n):
        n: char count
    Auxiliary space complexity: O(n)
    Tags:
        DS: list
        A: iteration
    """
    
    def encode(self, words: list[str]) -> str:
        res = []
        
        for word in words:
            res.append(f"${(len(word))}\r\n")
            res.append(f"{word}\r\n")
        
        return "".join(res)

    def decode(self, text: str) -> list[str]:
        res = []
        
        for idx, item in enumerate(text.split("\r\n")):
            if idx % 2:
                res.append(item)

        return res 