class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 != None:
            current.next = list1
        else:
            current.next = list2
        return head.next

def list_to_linkedlist(elements):
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

def linkedlist_to_list(node):
    elements = []
    while node:
        elements.append(node.val)
        node = node.next
    return elements

l1 = list_to_linkedlist([2, 5, 8, 9])
l2 = list_to_linkedlist([1, 2, 4, 5, 7])

solution = Solution()
merged_head = solution.mergeTwoLists(l1, l2)
merged_list = linkedlist_to_list(merged_head)
print(merged_list)
