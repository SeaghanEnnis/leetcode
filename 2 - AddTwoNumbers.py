class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(val = -1, next=None)
        temp = res
        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val + carry
            mod = sum % 10
            carry = sum // 10
            #print(mod)
            res.next = ListNode(val = mod, next=None)
            res = res.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + carry
            mod = sum % 10
            carry = sum // 10
            #print(mod)
            res.next = ListNode(val = mod, next=None)
            res = res.next
            l1 = l1.next
   
        while l2:
            sum = l2.val + carry
            mod = sum % 10
            carry = sum // 10
            #print(mod)
            res.next = ListNode(val = mod, next=None)
            res = res.next
            l2 = l2.next

        print(carry)
        if(carry != 0):
            res.next = ListNode(val = carry, next=None)
            res = res.next

        return temp.next