# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        levelOrder 를 통해서 가장 우측에 있는 노드의 값을 출력해야 함
        큐에 뎁스와 함께 노드를 넣고 뎁스가 바뀌면 이전 값에서 가장 우측에 있는 값을 추가
        """
        if root is None:
            return []

        result = [root.val]

        tree = root
        depth_check = 0
        level_nodes = [tree.val]
        q = deque([[tree, 0]])
        while q:
            node, depth = q.popleft()

            # 새로운 뎁스를 탐색하게 되면, level 에서 가장 우측 값을 결과에 추가
            # cur_depth, level_nodes 초기화
            if depth > depth_check:
                result.append(level_nodes[-1])

                depth_check = depth
                level_nodes = []

            # 자식 노드들 추가
            if node.left:
                q.append([node.left, depth + 1])
                level_nodes.append(node.left.val)
            if node.right:
                q.append([node.right, depth + 1])
                level_nodes.append(node.right.val)

        return result
