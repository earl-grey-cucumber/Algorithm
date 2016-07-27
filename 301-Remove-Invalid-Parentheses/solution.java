public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> result = new ArrayList<String>();
        Queue<String> queue = new LinkedList<String>();
        Set<String> visited = new HashSet<String>();
        queue.add(s);
        visited.add(s);
        boolean found = false;
        while(!queue.isEmpty()) {
            String cur = queue.poll();
            //visited.add(cur);
            if(isValid(cur)) {
                result.add(cur);
                found = true;
            }
            if(found) continue;
            for(int i = 0; i < cur.length(); i++) {
                if(cur.charAt(i) == '(' || cur.charAt(i) == ')') {
                    String temp = cur.substring(0, i) + cur.substring(i + 1);
                    if(!visited.contains(temp)) {
                        queue.add(temp);
                        visited.add(temp);
                    }
                }
            }
        }
        return result;
    }
    
    boolean isValid(String cur) {
        int left = 0, right = 0;
        for(int i = 0; i < cur.length(); i++) {
            if(cur.charAt(i) == '(') left++;
            if(cur.charAt(i) == ')') right++;
            if(left < right) return false;
        }
        return left == right;
    }
}