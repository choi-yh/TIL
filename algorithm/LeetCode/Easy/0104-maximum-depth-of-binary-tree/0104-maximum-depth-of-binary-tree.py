# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root == None:
            return depth

        same_depth_nodes = [root]
        while same_depth_nodes:
            depth += 1

            tmp_depth_nodes = []
            for nodes in same_depth_nodes:
                if nodes.left != None:
                    tmp_depth_nodes.append(nodes.left)
                
                if nodes.right != None:
                    tmp_depth_nodes.append(nodes.right)

            same_depth_nodes = tmp_depth_nodes

        return depth