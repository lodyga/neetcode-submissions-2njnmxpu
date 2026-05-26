class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode()

    def add(self, val: int) -> None:
        node = self.head

        while node.next:
            if node.next.val == val:
                return
            node = node.next

        node.next = ListNode(val)

    def has(self, val: int) -> bool:
        node = self.head

        while node.next:
            if node.next.val == val:
                return True
            node = node.next

        return False

    def discard(self, val: int) -> None:
        node = self.head

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                return
            node = node.next


class MyHashSet:
    """
    Time complexity:
        constructor: O(CAPACITY)
        add: avg O(1)
        contains: avg O(1)
        remove: avg O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: linked list, hash set
        A: iteration
    """

    CAPACITY = 10**4

    def __init__(self) -> None:
        self.buckets = [LinkedList() for _ in range(self.CAPACITY)]

    def _get_hash_key(self, val: int) -> int:
        return val % self.CAPACITY

    def _get_linked_list(self, val: int) -> LinkedList:
        hash_key = self._get_hash_key(val)
        return self.buckets[hash_key]

    def add(self, val: int) -> None:
        linked_list = self._get_linked_list(val)
        linked_list.add(val)

    def contains(self, val: int) -> bool:
        linked_list = self._get_linked_list(val)
        return linked_list.has(val)

    def remove(self, val: int) -> None:
        linked_list = self._get_linked_list(val)
        linked_list.discard(val)


