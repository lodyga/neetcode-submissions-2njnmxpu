class MyHashSet:
    """
    Time complexity:
        constructor: O(CAPACITY)
        add: avg O(1)
        contains: avg O(1)
        remove: avg O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: list, hash set
        A: iteration
    """

    CAPACITY = 10**4

    def __init__(self) -> None:
        self.buckets = [[] for _ in range(self.CAPACITY)]

    def _get_hash_key(self, val: int) -> int:
        return val % self.CAPACITY

    def _get_list(self, val: int) -> list:
        hash_key = self._get_hash_key(val)
        return self.buckets[hash_key]

    def _get_index(self, val: int) -> int:
        bucket = self._get_list(val)

        try:
            idx = bucket.index(val)
        except ValueError:
            idx = -1

        return idx

    def add(self, val: int) -> None:
        if not self.contains(val):
            bucket = self._get_list(val)
            bucket.append(val)

    def contains(self, val: int) -> bool:
        return self._get_index(val) != -1

    def remove(self, val: int) -> None:
        idx = self._get_index(val)

        if idx != -1:
            bucket = self._get_list(val)
            bucket.pop(idx)
