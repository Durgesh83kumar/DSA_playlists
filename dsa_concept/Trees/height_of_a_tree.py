from genericTreesInput import predefined_generic_tree_inputs

def height_of_a_tree(root):
    if(root==None):
        return 0
    
    height = 1
    max_child_height = 0

    for eachChild in root.children:
        max_child_height = max(max_child_height,height_of_a_tree(eachChild))

    height = height + max_child_height

    return height

root1, root2, root3 = predefined_generic_tree_inputs()

print(height_of_a_tree(root1))
print(height_of_a_tree(root2))
print(height_of_a_tree(root3))