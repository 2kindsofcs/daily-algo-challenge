import java.util.LinkedList;

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int rowSize = image.length;
        if (image.length == 0) {
            return image;
        }
        int colSize = image[0].length;
        
        if (colSize == 0) {
            return image;
        }
        boolean[][] visited = new boolean[rowSize][colSize];
        int[][] retImage = image;
        int color = image[sr][sc];

        LinkedList<int[]> queue = new LinkedList<int[]>();  

        visited[sr][sc] = true;
        int[] arr = {sr,sc};
        queue.add(arr);
        
        while (queue.size() != 0) {
            int[] retarr = queue.poll();
            int x = retarr[0];
            int y = retarr[1];

            if (image[x][y] == color) {
                retImage[x][y] = newColor;
                // four adjacent nodes with same num 
                if (x-1 > -1 && x-1 < rowSize) {
                    if (visited[x-1][y] == false) {
                        visited[x-1][y] = true; 
                        int[] newarr = {x-1,y};
                        queue.add(newarr);
                    }
                }
                if (y-1 > -1 && y-1 < colSize) {
                    if (visited[x][y-1] == false) {
                        visited[x][y-1] = true; 
                        int[] newarr = {x,y-1};
                        queue.add(newarr);
                    }
                }

                if (y+1 > -1 && y+1 < colSize) {
                    if (visited[x][y+1] == false) {
                        visited[x][y+1] = true; 
                        int[] newarr = {x,y+1};
                        queue.add(newarr);
                    }
                }

                if (x+1 > -1 && x+1 < rowSize) {
                    if (visited[x+1][y] == false) {
                        visited[x+1][y] = true; 
                        int[] newarr = {x+1,y};
                        queue.add(newarr);
                    }
                }
            }

            
        }
        return retImage;

    }
}

/*
Runtime: 1 ms, faster than 90.81% of Java online submissions for Flood Fill.
Memory Usage: 45 MB, less than 56.01% of Java online submissions for Flood Fill.
*/

