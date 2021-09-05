# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderHelper(root,[])
    
    def postorderHelper(self,root,res):
        if not root:
            return 
        self.postorderHelper(root.left,res)
        self.postorderHelper(root.right,res)
        res.append(root.val)
        return res


## Time: O(N)
## Space: O(1)
        
        
        