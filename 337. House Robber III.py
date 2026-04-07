# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return(max(self.dfs(root)))
    
    def dfs(self, pos):
        if pos.left != None and pos.right != None:
            r = self.dfs(pos.right)
            l = self.dfs(pos.left)
            return [pos.val + r[1] + l[1], max(r[1],r[0])+max(l[0],l[1])]
        elif pos.left != None and pos.right == None:
            l = self.dfs(pos.left)
            return [pos.val+l[1], max(l[0], l[1])]
        elif pos.left == None and pos.right != None:
            r = self.dfs(pos.right)
            return [pos.val+r[1], max(r[0], r[1])]
        else:
            return [pos.val, 0]
