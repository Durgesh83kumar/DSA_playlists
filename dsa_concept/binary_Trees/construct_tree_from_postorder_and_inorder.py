from predefinedBT import predefined_binary_tree_inputs, BinaryTreeNode, print_level_wise

def construct_tree_from_inorder_and_postorder(inorder, postorder, inS,inE, poS, poE):
    if(inS>inE or poS>poE): # Base condition
        return None
    
    root_data = postorder[poE]
    root = BinaryTreeNode(root_data)

    rootIndexInInorder = -1
    for i in range(inS, inE + 1):
        if(inorder[i] == root_data):
            rootIndexInInorder = i
            break
    
    if(rootIndexInInorder == -1):
        print("root not found in Inorder, please check the logic")
        return None
    
    linS = inS
    linE = rootIndexInInorder - 1
    lpoS = poS
    lpoE = lpoS + (linE - linS)

    rinS = rootIndexInInorder + 1
    rinE = inE
    rpoS = lpoE + 1
    rpoE = poE - 1

    root.left = construct_tree_from_inorder_and_postorder(inorder, postorder, linS, linE, lpoS, lpoE)
    root.right = construct_tree_from_inorder_and_postorder(inorder, postorder, rinS, rinE, rpoS, rpoE)

    return root


postorder = [4, 5, 2, 6, 3, 1]
inorder = [4, 2, 5, 1, 3, 6]

n = len(inorder)
root = construct_tree_from_inorder_and_postorder(inorder, postorder, 0, n-1, 0, n-1)
print_level_wise(root)