class Solution:
  def flatten(self, root: Optional[TreeNode]) -> None:
    current = root
    while current:
      if current.left:
        # Find the rightmost node of the left subtree
        predecessor = current.left
        while predecessor.right:
          predecessor = predecessor.right
        
        # Connect original right subtree to the predecessor's right
        predecessor.right = current.right
        # Move left subtree to the right side
        current.right = current.left
        current.left = None
      
      current = current.right
