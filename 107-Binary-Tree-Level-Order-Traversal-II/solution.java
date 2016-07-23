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
    public ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        if(root==null) return res;
        dfs(res,root,0);
        return res;
    }
    
    public void dfs(ArrayList<ArrayList<Integer>> res,TreeNode root, int k) {
        if(root==null) return;
        if(k==res.size()) res.add(0,new ArrayList<Integer>());
        res.get(res.size()-k-1).add(root.val);
        dfs(res,root.left,k+1);
        dfs(res,root.right,k+1);
    }
}