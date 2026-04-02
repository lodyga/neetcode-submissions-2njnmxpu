class Solution:

    def encode(self, strs: List[str]) -> str:
        return ["Τ" + word + "Τ" for word in strs]

    def decode(self, s: str) -> List[str]:
        return [word[1:-1] for word in s]
