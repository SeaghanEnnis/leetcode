class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return

        current = head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous