public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<String>();
        if(s.length() < 4 || s.length() > 12) return result;
        dfs(s, result, "", 0, 0);
        return result;
    }
    
    void dfs(String s, List<String> result, String temp, int index, int k) {
        if(index == s.length()) {
            if(k == 4) result.add(temp);
            return;
        }
        for(int i = 1; i <= 3 && index + i <= s.length(); i++) {
            String substr = s.substring(index, index + i);
            if(isValid(substr)) {
                if(temp.length() == 0) dfs(s, result, temp + substr, index + i, k + 1);
                else dfs(s, result, temp + "." + substr, index + i, k + 1);
            }
        }
    }
    
    boolean isValid(String s) {
        if(s == null || s.length() == 0) return false;
        if(s.charAt(0) == '0') return s.equals("0");
        return Integer.valueOf(s) > 0 && Integer.valueOf(s) <= 255;
    }
}