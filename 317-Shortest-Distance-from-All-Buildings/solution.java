public class Solution {
    class Point{
		int x;
		int y;
		public Point(int x, int y){
			this.x=x;
			this.y=y;
		}
	}
	
	boolean isValid(int i,int j, boolean[][]visited,int[][] grid,int m, int n) {		
		if(i<0||i>=m||j<0||j>=n) return false;
		if(grid[i][j] == 2 || grid[i][j] == 1) return false;
		if(visited[i][j]) return false;
		return true;
	}
	
    public int shortestDistance(int[][] grid) {
        HashSet<Point> robot = new HashSet<Point>();
        int m = grid.length, n = grid[0].length;
		//boolean[][] blocker = new boolean[m][n];
		for(int i = 0; i < m; i++) {
		    for(int j = 0; j < n; j++) {
		        if(grid[i][j] == 1) robot.add(new Point(i, j));
		        //if(grid[i][j] == 2) blocker[i][j] = true;
		    }
		}
		int[][] temp = new int[m][n];
		int[][] count = new int[m][n];
        for(Point p:robot) {
			LinkedList<Point> q = new LinkedList<Point>();
			boolean[][] visited=new boolean[m][n];
			q.offer(p);		
			visited[p.x][p.y]=true;
			int len=0;
			while(!q.isEmpty()) {
				int size =q.size();
				for(int i=0;i<size;i++) {
					Point cur = q.poll();					
					temp[cur.x][cur.y]+=len;
					count[cur.x][cur.y]++;
					if(isValid(cur.x+1,cur.y,visited,grid,m,n)) {						
						q.offer(new Point(cur.x+1,cur.y));
						visited[cur.x+1][cur.y]=true;
					}
					if(isValid(cur.x-1,cur.y,visited,grid,m,n)) {
						q.offer(new Point(cur.x-1,cur.y));
						visited[cur.x-1][cur.y]=true;
					}
					if(isValid(cur.x,cur.y-1,visited,grid,m,n)) {
						q.offer(new Point(cur.x,cur.y-1));
						visited[cur.x][cur.y-1]=true;
					}
					if(isValid(cur.x,cur.y+1,visited,grid,m,n)) {
						q.offer(new Point(cur.x,cur.y+1));
						visited[cur.x][cur.y+1]=true;
					}
				}
				len++;
			}
		}
		
		int min=Integer.MAX_VALUE;
		int x = 0, y = 0;
		for(int i=0;i<m;i++) {
			for(int j=0;j<n;j++) {
				if(grid[i][j] == 0 && temp[i][j] < min && count[i][j] == robot.size()) {
				    min=temp[i][j];
				    x = i;
				    y = j;
				}
			}
		}
		return (min == Integer.MAX_VALUE || min == 0) ? -1 : min;
    }
}