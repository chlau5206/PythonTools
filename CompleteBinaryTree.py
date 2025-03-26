# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
###############################################
# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
###############################################

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        if root :   # is not  empty
            self.root = root
            # self.queue.append(root)
        else: 
            self.root = None

    def insert(self, val: int) -> int:
        root = self.get_root()
        if root is None: 
            root = TreeNode(val)
            return 0
        else: 
            queue = [root]
            while queue is not None:
                currNode = queue[0]
                if currNode.val is not None:
                    if currNode.left: 
                        queue.append(currNode.left)
                    else:
                        currNode.left = TreeNode(val)
                        return currNode.val
                    if currNode.right: 
                        queue.append(currNode.right)
                    else:
                        currNode.right = TreeNode(val)
                        return currNode.val
                queue.remove(currNode)

    def get_root(self) -> Optional[TreeNode]:
        return self.root


class Solution:
    def build_tree(self, values):
        if not values:
            return None

        # Use a queue to hold nodes and their positions
        root = TreeNode(values[0])
        queue = [root]
        i = 1

        while i < len(values):
            current = queue.pop(0)

            # Assign left child
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            # Assign right child
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

        return root

    # Simple function to traverse and visualize the tree (optional)
    def preorder_traversal(self, root):
        if not root:
            return 'null'
        return str([root.val]) + s.preorder_traversal(root.left) + s.preorder_traversal(root.right)

    def level_order_traversal(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])  # Use a deque for efficient FIFO queue operations

        while queue:
            current = queue.popleft()
            result.append(current.val)

            # Add left child to queue if it exists
            if current.left:
                queue.append(current.left)
            
            # Add right child to queue if it exists
            if current.right:
                queue.append(current.right)

        return result


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        root_left = p
        root_right = q

        if not ((root_left ^ root_right) and  (root_left.val ^ root_right.val)):
            return False
        
        return False
        


if __name__ == '__main__':
    s = Solution()
    null = None
    data = [1, null, 4,3,5]
    tree_root = s.build_tree(data)

    print(s.preorder_traversal(tree_root))  # Output: [1, 2]

    # Perform level-order traversal
    print(s.level_order_traversal(tree_root))  # Output: [1, 2]
