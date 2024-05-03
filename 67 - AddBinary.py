class Solution(object):
    def addBinary(self, a, b):
        s = []
        carry = 0
        pos1 = len(a) - 1
        pos2 = len(b) - 1

        while pos1 >= 0 or pos2 >= 0 or carry:

            if pos1 >= 0:
                carry += int(a[pos1])
                pos1 -= 1
            if pos2 >= 0:
                carry += int(b[pos2])
                pos2 -= 1

            s.append(str(carry % 2))
            carry //= 2

        return ''.join(reversed(s))