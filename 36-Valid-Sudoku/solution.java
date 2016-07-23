public class Solution {
    public boolean isValidSudoku(char[][] board) {
        if(board==null|board.length==0) return true;
        String s = "";
        int m=board.length, n=board[0].length;
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                s += board[i][j];
            }
        }
        return helper(s);
    } 
    
    boolean helper(String s) {
        if(s==null || s.length() != 81) return false;
        for(int i=0;i<9;i++) {
            Set<Character> set = new HashSet<Character>();           
            for(int j=0;j<9;j++) {
            	char c = s.charAt(i * 9 + j);
                if(c!='.'&&!set.add(c)) return false;
            }
        }
        
        for(int i=0;i<9;i++) {
            Set<Character> set = new HashSet<Character>();
            for(int j=0;j<9;j++) {
            	char c = s.charAt(j * 9 + i);
                if(c!='.'&&!set.add(c)) return false;
            }
        }
        
        for(int i=0;i<3;i++) {
            for(int j=0;j<3;j++) {
                HashSet<Character> set = new HashSet<Character>();
                for(int m=0;m<3;m++) {
                    for(int n=0;n<3;n++) {
                    	int row = 3 * i + m, col = 3 * j + n;
                    	char c = s.charAt(row * 9 + col);
                        if(c!='.'&&!set.add(c)) return false;
                    }
                }
            }
        }
        return true;
    }
}