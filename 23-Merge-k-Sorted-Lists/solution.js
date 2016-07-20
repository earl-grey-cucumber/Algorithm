/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    int n = lists.length;
    if(n == 0) return null;
    int i = 0, j = n - 1;
    Comparator<ListNode> c = new Comparator<ListNode>() {
        public int compare(ListNode n1, ListNode n2) {
            return n1.val - n2.val;
        }  
    };
    PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(n, c);
    for(ListNode l: lists) {
        if(l != null) pq.add(l);
    }
    ListNode dummy = new ListNode(0);
    ListNode pre = dummy;
    while(!pq.isEmpty()) {
        ListNode cur = pq.poll();
        pre.next = cur;
        pre = pre.next;
        if(cur.next != null) pq.add(cur.next);
    }
    return dummy.next;
};