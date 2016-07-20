public class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        List<String> result = new ArrayList<String>();
        if(s == null || s.length() <= 1) return result;
        if(s.length() == 2 && !s.equals("++")) return result;
        int n = s.length();
        for(int i = 1; i < n; i++) {
            char pre = s.charAt(i - 1);
            char cur = s.charAt(i);
            if(pre == cur && pre == '+') {
                result.add(s.substring(0, i -1) + "--" + s.substring(i + 1, n));
            }
        }
        return result;
    }
}