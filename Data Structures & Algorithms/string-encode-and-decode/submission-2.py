class Solution:

    def encode(self, strs: List[str]) -> str:
        return ["Δ" + word for word in strs]

    def decode(self, s: str) -> List[str]:
        return [word[1:] for word in s]
