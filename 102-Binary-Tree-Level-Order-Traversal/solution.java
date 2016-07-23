/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(root==null) return res;
        dfs(res,root,0);
        return res;
    }
    
    public void dfs(List<List<Integer>> res,TreeNode root, int k) {
        if(root==null) return;
        if(k==res.size()) res.add(new ArrayList<Integer>());
        res.get(k).add(root.val);
        dfs(res,root.left,k+1);
        dfs(res,root.right,k+1);
    }
}