from __future__ import annotations

# python3 -m pydoc deque

input = '''\

l1 = [2,4,3], l2 = [5,6,4]

ouput = [7, 0, 8]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

ouput = [8,9,9,9,0,0,0,1]
'''


class BrutalForce:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) \
     -> Optional[ListNode]:
        list1 = [i for i in l1[::-1]]
        num1 = ''
        for n1 in list1:
            num1 += str(n1)
        num1 = int(num1)
        print(num1)

        stack2 = []
        num2 = ''
        for n2 in l2:
            stack2.append(n2)
        while stack2:
            d = stack2.pop()
            num2 += str(d)
        num2 = int(num2)
        print(num2)

        sum = num1 + num2
        output = [i for i in reversed(str(sum))]
        print(output)

'''
start from the head(the least significant digit/smaller)
Time: O(n + m)
Space: O(n + m)
'''
class ListNode:
    def __init__(self, val = 0, next = None):
        # ListNode(0) val: the node indices in the nodes
        self.val = val
        self.next = next
    def __repr__(self):
        return 'ListNode(val, next = ' + str(self.val) + ', {' + str(self.next) + "})"

class LinkedNode:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) \
     -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        # loop thru to get the end of either
        while l1 or l2 or carry: # 8 + 7 edge cases
            v1 = l1.val if l1 else 0 # head
            v2 = l2.val if l2 else 0

            # new digit val
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)  # as in one place we have to put a single digit

            # update pointers
            curr = curr.next
            # print(curr)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


def list_to_listnode(arr):
    if len(arr) < 1:
        return None
    if len(arr) == 1:
        return ListNode(arr[0])

    return ListNode(arr[0], next = list_to_listnode(arr[1:]))

l_1 = [2,4,3]
l_2 = [5,6,4]

l1 = list_to_listnode(l_1)
l2 = list_to_listnode(l_2)
# l1 = ListNode((val for i, val in enumerate(l_1)), (val for i, val in enumerate(l_1[1:])))
# l2 = ListNode((val for i, val in enumerate(l_2)), (val for i, val in enumerate(l_2[1:])))

n = LinkedNode()
print(n.addTwoNumbers(l1, l2))






# end
