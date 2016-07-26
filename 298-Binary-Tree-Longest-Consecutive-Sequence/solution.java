/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int longestConsecutive(TreeNode root) {
        if(root == null) return 0;
        int[] result = {0};
        helper(root, result);
        return result[0];
    }
    
    int helper(TreeNode root, int[] result) {
        if(root == null) return 0;
        int len = 1;
        int left = helper(root.left, result);
        int right = helper(root.right, result);
        if(root.left != null && root.left.val - 1 == root.val) len = Math.max(1, left + 1);
        if(root.right != null && root.right.val - 1 == root.val) len = Math.max(1, right + 1);
        result[0] = Math.max(len, result[0]);
        return len;
    }
  /*int max;

  public int longestConsecutive(TreeNode root) {
    max = 0;
    helper(root);
    return max;
  }

  int helper(TreeNode root) {
    if (root == null) return 0;

    int len = 1;
    int left = helper(root.left);
    int right = helper(root.right);

    if (root.left != null && root.val == root.left.val - 1) {
      len = Math.max(len, left + 1);
    }

    if (root.right != null && root.val == root.right.val - 1) {
      len = Math.max(len, right + 1);
    }

    max = Math.max(len, max);

    return len;
  }*/
}