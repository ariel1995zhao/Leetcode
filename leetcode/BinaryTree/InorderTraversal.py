# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderHelper(root,[])
    
    def inorderHelper(self,root,res):
        if root is None:
            return 
        self.inorderHelper(root.left,res)
        res.append(root.val)
        self.inorderHelper(root.right,res)
        return res
    

## time : O(N)
## Space: O(1)