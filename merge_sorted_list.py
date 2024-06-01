
class ListNode():
    def __init__(self, val = 0,next = None):
        self.val = val
        self.next = next

# The list_to_linkedlist function converts a list to a linked list.
def list_to_linkedlist(elements):
    head = ListNode(elements[0])
    current = head
    for numbers in elements:
        current.next = ListNode(numbers)
        current = current.next
    return head

class SortList():
    def merge_sorted_list(self,list1,list2):
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
        return head

# The linkedlist_to_list function converts a linked list back to a Python list.
def linkedlist_to_list(merge):
    list = []
    while merge:
        list.append(merge.val)
        merge = merge.next
    return list


l1 = list_to_linkedlist([2, 5, 8, 9])
l2 = list_to_linkedlist([1, 2, 4, 5, 7])
sort = SortList()
merge = sort.merge_sorted_list(l1,l2)
print(linkedlist_to_list(merge))

