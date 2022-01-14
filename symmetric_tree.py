class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

leftnode = TreeNode(val=2, left=TreeNode(3), right=TreeNode(4))
rightnode = TreeNode(val=2, left=TreeNode(4), right=TreeNode(3))
root = TreeNode(val=1, left=leftnode, right=rightnode)

leftnode2 = TreeNode(val=2, right=TreeNode(3))
rightnode2 = TreeNode(val=2, right=TreeNode(3))
root2 = TreeNode(val=1, left=leftnode2, right=rightnode2)

def isSymmetric(root: TreeNode) -> bool:

    def tree_to_list(root: TreeNode):
        list1 = []
        if root:
            listleft = tree_to_list(root.left)
            listright = tree_to_list(root.right)
            list1 = listleft + [root.val] + listright   
        
        return list1


    return list == listsym

def tree_to_list2(root):
    res = []
    current_floor = [root]
    while not all(i is None for i in current_floor):
        res += [node.val for node in current_floor]
        new_floor = []
        for node in current_floor:
            new_floor += [node.left, node.right]
        current_floor = new_floor
    return res

def tree_to_list3(root):
    res = []
    current_floor = [root]
    while not all(i is None for i in current_floor):
        res += [node.val if node else None for node in current_floor]
        new_floor = []
        for node in current_floor:
            if node:
                new_floor += [node.left, node.right]
            else:
                new_floor += [None, None]
        current_floor = new_floor
    return res

#print(tree_to_list3(root2))

def sym(root: list) -> bool:    
    x = str(tree_to_list3(root))
    for i in range(len(x) // 2):
        if x[i] != x[-i-1]:
            return False
    return True

root = [1,2,2,3,4,4,3]
     #  0 1 2 3 4 5 6

sym(root)

def list_to_tree(root: list) -> TreeNode:
    #on découpe la liste en étages, chaque nouvel étage comprend 2x plus d'éléments que le précédent
    floornb=111

    while root:
        current_floor=[root[0:floornb]]
        del root[0:floornb]
        for i in current_floor:
            node = TreeNode(val=i, left=root[index de i], right=root[index de i +1])

    reversedroot = reversed(root)
    current_node = None
    for val in reversedroot:
        new_node = TreeNode(val=val, left=current_node, right=)
        current_node = new_node
    return current_node

    for i in root:
        i = TreeNode(val=i, left=i+1, right=i+3)

def list_to_tree3(root:list) -> TreeNode:
    if val == None:
        return
    new_node=TreeNode(val,)
    new_node.left=list_to_tree3(val, )
    new_node.right=list_to_tree3(val)
    return new_node