from genericTreesInput import predefined_generic_tree_inputs


def preOrder_Traversal(root):
    if(root is None): # Edge Case
        return
    
    print(root.data, end = " ")

    for eachChild in root.children:
        preOrder_Traversal(eachChild)



def postOrder_Traversal(root):
    if(root is None): # Edge Case
        return
    
    for eachChild in root.children:
        postOrder_Traversal(eachChild)

    print(root.data, end = " ")



root1, root2, root3 = predefined_generic_tree_inputs()
print("Preoder Traversal: ")
preOrder_Traversal(root1)
print("\nPostorder Traversal: ")
postOrder_Traversal(root1)