from predefinedBT import predefined_binary_tree_inputs

root1,root2,root3 = predefined_binary_tree_inputs()

def predorder_traversal(root):
    if(root is None):
        return
    
    print(root.data, end = " ")
    predorder_traversal(root.left)
    predorder_traversal(root.right)


predorder_traversal(root1)
print()

def postorder_traversal(root):
    if(root is None):
        return
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)

    print(root.data, end = " ")

postorder_traversal(root1)

print()

def inorder_traversal(root):
    if(root is None):
        return
    
    inorder_traversal(root.left)
    print(root.data, end = " ")
    inorder_traversal(root.right)

inorder_traversal(root1)