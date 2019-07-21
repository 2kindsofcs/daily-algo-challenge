import java.lang.*;

class Solution {
    public int[][] imageSmoother(int[][] M) {
        int rowLength = M.length;
        int colLength = M[0].length; 
        int[][] retM = new int[rowLength][colLength];

        for (int i = 0; i < M.length; i ++) {
            for (int j = 0; j < M[i].length; j ++) {
                int sum = 0; 
                int count = 1;
                sum += M[i][j];
                
                if (checkRange(i-1,j-1,rowLength,colLength)) {
                    sum += M[i-1][j-1];
                    count += 1;
                }
                if (checkRange(i-1,j,rowLength,colLength)) {
                    sum += M[i-1][j];
                    count += 1;
                }
                if (checkRange(i-1,j+1,rowLength,colLength)) {
                    sum += M[i-1][j+1];
                    count += 1;
                }
                if (checkRange(i,j-1,rowLength,colLength)) {
                    sum += M[i][j-1];
                    count += 1;
                }
                if (checkRange(i,j+1,rowLength,colLength)) {
                    sum += M[i][j+1];
                    count += 1;
                }
                if (checkRange(i+1,j-1,rowLength,colLength)) {
                    sum += M[i+1][j-1];
                    count += 1;
                }
                if (checkRange(i+1,j,rowLength,colLength)) {
                    sum += M[i+1][j];
                    count += 1;
                }
                if (checkRange(i+1,j+1,rowLength,colLength)) {
                    sum += M[i+1][j+1];
                    count += 1;
                }
                double div = (double)sum/count;
                retM[i][j] = (int)Math.floor(div);
            }
        }
        return retM; 
    }
    
    public boolean checkRange(int i, int j, int rowLength, int colLength) {
        if (i >= 0 && i < rowLength && j >= 0 && j < colLength) {
            return true; 
        } else {
            return false; 
        }
    }
}