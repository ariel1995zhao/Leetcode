# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ## first itself, then left, and right
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preorderHelper(root,[])
    
    def preorderHelper(self,root,res):
        if not root:
            return 
        res.append(root.val)
        self.preorderHelper(root.left,res)
        self.preorderHelper(root.right,res)
        return res
        

## Time: O(N)
## Space: O(1)