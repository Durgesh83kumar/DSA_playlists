from genericTreesInput import predefined_generic_tree_inputs

def count_nodes(root):
    if(root==None):
        return 0
    
    numberOfNodes = 1

    for eachChild in root.children:
        numberOfNodes = numberOfNodes + count_nodes(eachChild)

    return numberOfNodes

root1, root2, root3 = predefined_generic_tree_inputs()

print(count_nodes(root1))
print(count_nodes(root2))
print(count_nodes(root3))
