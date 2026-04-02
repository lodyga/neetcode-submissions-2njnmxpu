class Solution:

    def encode(self, strs: List[str]) -> str:
        return ["Τ" + word for word in strs]

    def decode(self, s: str) -> List[str]:
        return [word[1:] for word in s]
