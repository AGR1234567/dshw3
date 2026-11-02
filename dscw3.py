class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

    # def count(self):
    #     if self is None:
    #         return 0
    #     return 1 + self.left.count() + self.right.count()

def count(root):
    if root is None:
        return 0
    return 1+count(root.left)+count(root.right)

root=TreeNode(10)
root.left=TreeNode(5)
root.right=TreeNode(15)

a=count(root)
print(a)