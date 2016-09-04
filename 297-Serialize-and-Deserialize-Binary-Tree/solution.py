# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        def serializeHelper(node):
            if not node:
                vals.append('#')
            else:
                vals.append(str(node.val))
                serializeHelper(node.left)
                serializeHelper(node.right)
        vals = []
        serializeHelper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def deserializeHelper():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = deserializeHelper()
                node.right = deserializeHelper()
                return node
        def isplit(source, sep):
            sepsize = len(sep)
            start = 0
            while True:
                idx = source.find(sep, start)
                if idx == -1:
                    yield source[start:]
                    return
                yield source[start:idx]
                start = idx + sepsize
        vals = iter(isplit(data, ' '))
        return deserializeHelper()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))