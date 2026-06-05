from predefinedBT import predefined_binary_tree_inputs

def height(root):
    if(root is None):
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    heightOfTree = 1 + max(left_height,right_height)

    return heightOfTree


def diameter_of_a_tree(root):
    if(root is None):
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    left_diameter = diameter_of_a_tree(root.left)
    right_diameter = diameter_of_a_tree(root.right)

    ans = max(left_diameter, right_diameter, leftHeight+rightHeight)

    return ans

root1, root2, root3 = predefined_binary_tree_inputs()

print(diameter_of_a_tree(root1))