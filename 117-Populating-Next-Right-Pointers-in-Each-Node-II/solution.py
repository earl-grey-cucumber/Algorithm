/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        if(root==null) return;
        TreeLinkNode cur = root;
        while(cur != null){
            TreeLinkNode level = cur, first = null, pre = null;
            while(level != null) {
                if(level.left != null) {
                    if(first == null) first = level.left;
                    if(pre == null) pre = level.left;
                    else {
                        pre.next = level.left;
                        pre = pre.next;
                    }
                } 
                if(level.right != null) {
                    if(first == null) first = level.right;
                    if(pre == null) pre = level.right;
                    else {
                        pre.next = level.right;
                        pre = pre.next;
                    }
                } 
                level = level.next;
            }
            cur = first;
        }
    }
}