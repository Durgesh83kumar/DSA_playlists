from predefinedBSTs import create_predefined_bsts_manual

root1, root2, root3 = create_predefined_bsts_manual()




def search_in_BST(root, value):
    if(root is None):
        return False
    
    if(root.data == value):
        return True
    
    if(root.data > value):
        return search_in_BST(root.left, value)
    
    if(root.data < value):
        return search_in_BST(root.right, value)


print(search_in_BST(root2, 5))