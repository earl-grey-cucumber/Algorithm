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
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        List<Integer> result = new ArrayList<Integer>();
        Stack<Integer> left = new Stack<Integer>();
        Stack<Integer> right = new Stack<Integer>();
        helper1(left, root, target);
        helper2(right, root, target);
        while(k-- > 0) {
            if(left.isEmpty()) {
                result.add(right.pop());
            } else if(right.isEmpty()) {
                result.add(left.pop());
            } else if(Math.abs(target - left.peek()) < Math.abs(right.peek() - target)) {
                result.add(left.pop());
            } else {
                result.add(right.pop());
            }
        }
        return result;
    }
    
    void helper1(Stack<Integer> left, TreeNode root, double target) {
        if(root == null) return;
        helper1(left, root.left, target);
        if(root.val > target) return;
        left.push(root.val);
        helper1(left, root.right, target);
    }
    
    void helper2(Stack<Integer> right, TreeNode root, double target) {
        if(root == null) return;
        helper2(right, root.right, target);
        if(root.val <= target) return;
        right.push(root.val);
        helper2(right, root.left, target);
    }
}