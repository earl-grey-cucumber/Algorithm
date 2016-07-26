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
    public int closestValue(TreeNode root, double target) {
        double closest = Math.abs(root.val - target);
        int value = root.val;
        TreeNode current = root;
        while (current != null) {
            if (compare(closest, Math.abs(current.val-target)) > 0) {
                closest = Math.abs(current.val-target);
                value = current.val;
            }
            if (compare(current.val, target) < 0)
                current = current.right;
            else if(compare(current.val, target) > 0)
                current = current.left;
            else break;
        }
        return value; 
    }
    
    int compare(double val1, double val2) {
        double temp = val1 - val2;
        if(temp < -1e-10) return -1;
        if(temp > 1e-10) return 1;
        return 0;
    }
}