public class NumArray {
    class SegmentTreeNode {
    	public int start, end;
    	public SegmentTreeNode left, right;
    	public int sum;
    	public SegmentTreeNode(int start, int end) {
    	   this.start = start;
    	   this.end = end;
    	}
    	public SegmentTreeNode(int start, int end, int sum) {
    	   this.start = start;
    	   this.end = end;
    	   this.sum = sum;
    	}
    }

    public SegmentTreeNode build(int[] A, int start, int end) {
        if(start > end) return null;
        SegmentTreeNode root = new SegmentTreeNode(start, end, A[start]);
        if(start == end) return root;
        
        int mid = start + (end - start) / 2;
        root.left = build(A, start, mid);
        root.right = build(A, mid + 1, end); 
        
        int sum = 0;
        if(root.left != null) sum = root.left.sum;  // cannot use root.sum+=root.left.sum
        if(root.right != null) sum += root.right.sum;
        root.sum = sum;
        return root;
    }

    private SegmentTreeNode root;
    public NumArray(int[] nums) {
        root = build(nums, 0, nums.length - 1);
    }

    void update(int i, int val) {
        modifyHelper(root, i, val);
    }

    public void modifyHelper(SegmentTreeNode root, int index, int value) {
        if(root == null || index < root.start || index > root.end) return;
        if(root.start == index && root.end == index) {
            root.sum = value;
            return;
        }
        int mid = root.start + (root.end - root.start) / 2;
        if(index <= mid) {
            modifyHelper(root.left, index, value);
        } else {
            modifyHelper(root.right, index, value);
        }
        int sum = 0;
        if(root.left != null) sum = root.left.sum;
        if(root.right != null) sum += root.right.sum;
        root.sum = sum;  //update sum at current node
    }
    
    public int sumRange(int i, int j) {
        return queryHelper(root, i, j);
    }
    
    public int queryHelper(SegmentTreeNode root, int start, int end) {
        if(root == null || start > end) return 0;
        if(root.start == start && root.end == end) return root.sum;  
        int mid = root.start + (root.end - root.start) / 2;
        if (mid + 1 > end) {
            return queryHelper(root.left, start, end);
        } else if (mid < start) {
            return queryHelper(root.right, start, end);
        } else {
            return queryHelper(root.left, start, mid) + queryHelper(root.right, mid + 1, end);
        }
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);