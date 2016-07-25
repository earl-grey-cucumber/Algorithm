# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = [root]
        result = str(root.val)
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                result += ","
                if cur.left:
                    queue.append(cur.left)
                    result += str(cur.left.val)
                else:
                    result += "#"
                result += ","
                if cur.right:
                    queue.append(cur.right)
                    result += str(cur.right.val)
                else:
                    result += "#"
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            size = len(queue)
            for j in range(size):
                cur = queue.pop(0)
                if nodes[i] != "#":
                    cur.left = TreeNode(int(nodes[i]))
                    queue.append(cur.left)
                i += 1
                if nodes[i] != "#":   
                    cur.right = TreeNode(int(nodes[i]))
                    queue.append(cur.right)
                i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))