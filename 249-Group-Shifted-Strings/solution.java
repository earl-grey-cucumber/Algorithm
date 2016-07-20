public class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        List<List<String>> result = new ArrayList<List<String>>();
        Map<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
        for(int i = 0; i < strings.length; i++) {
            String key = getCode(strings[i]);
            if(!map.containsKey(key)) map.put(key, new ArrayList<String>());
            map.get(key).add(strings[i]);
        }
        for(ArrayList<String> list: map.values()) {
            Collections.sort(list);
            result.add(list);
        }
        return result;
    }
    
    String getCode(String s) {
        if(s.length()==0) return "";
        StringBuilder sb = new StringBuilder();
        for(int  i = 1; i < s.length(); i++) {
            int dif = (s.charAt(i) - s.charAt(i - 1) + 26) % 26;
            sb.append(dif).append("#");
        }
        return sb.toString();
    }
}