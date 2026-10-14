# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        q = []
        cur = []

        level 1: cur = [1] -> append to res -> flush the cur
        level 2: same
        level 3: same

        until nothing inside q
        """
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(cur)

        return res
