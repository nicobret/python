class ListNode(object):
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

def list_to_listnode(l: list) -> ListNode:
    reversedl = reversed(l)
    current_node = None
    for val in reversedl:
        new_node = ListNode(val=val, next=current_node)
        current_node = new_node
    return current_node

def listnode_to_list(node: ListNode) -> list:
    newlist = []
    while node is not None:
        newlist.append(node.val)
        node = node.next
    return newlist

def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    else:
        if list1.val <= list2.val:
            return ListNode(val=list1.val, next=mergeTwoLists(list1.next, list2))
        else:
            return ListNode(val=list2.val, next=mergeTwoLists(list1, list2.next))

# def mergeTwoLists2(list1, list2):
    new_list = list1
    cur_node1 = list1
    cur_node2 = list2

    while cur_node2 != None:
        while cur_node1 != None:
            if cur_node2.val < cur_node1.val:
                new_list = cur_node2.val
                new_list.next = cur_node1
            else:
                cur_node1.next = cur_node2

        cur_node2 = cur_node2.next

l1 = [1,2,6,7,10,48]
l2 = [1,5,6,8,12]

# résultat attendu : 1,1,2,5,6,6,7,8,10,12,48

list1 = list_to_listnode(l1)
list2 = list_to_listnode(l2)

nouvelleliste1 = listnode_to_list(list1)

assert l1 == nouvelleliste1

print(listnode_to_list(mergeTwoLists(list1, list2)))