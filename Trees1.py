# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time complexity  - O(N)
# Space complexity - O(H) H-height of the subtree

# Traverse the left subtree first and right subtree
# Check if BST property is valid i.e the prev node should be less than current node at each level
# Use a stack to keep track of traversed nodes.

#Iterative solution
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        
        prev= float('-inf')
        
        stack=[]
        while root!=None or len(stack)>0:
            
            while root!=None:
                stack.append(root)
                root=root.left
            
            root=stack.pop()
            
            if prev >=root.val:
                return False
            
            prev=root.val
            root=root.right
        return True 
		
		
#Recursive solution

# Time complexity  - O(N)
# Space complexity - O(H) H-height of the subtree

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev=TreeNode(None)
        return self.inorder(root)
    
    def inorder(self,root):
        if root== None: return True
        
        if self.inorder(root.left) ==None:  return False
        
        if (self.prev.val and self.prev.val>=root.val): return False
    
        self.prev=root
        
        return self.inorder(root.right)