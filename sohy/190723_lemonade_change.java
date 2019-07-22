class Solution {
    public boolean lemonadeChange(int[] bills) {
        
        int i = 0;
        int numOfFives = 0;
        int numOfTens = 0; 
        
        while (i < bills.length) {
            if (bills[i] == 5) {
                numOfFives += 1; 
                i ++; 
                continue;
            } else if (bills[i] == 10) {
                if (numOfFives <= 0) {
                    return false; 
                } else {
                    numOfFives -= 1; 
                    numOfTens += 1;
                    i ++; 
                    continue; 
                }
            } else {
                if (numOfFives >= 1 && numOfTens >= 1) {
                    numOfFives -= 1; 
                    numOfTens -= 1;
                    i ++; 
                    continue;
                } else if (numOfFives >= 3) {
                    numOfFives -= 3; 
                    i ++; 
                    continue;
                } else {
                    return false; 
                }
            }
        }
    return true; 
        
    }
}

/*

Runtime: 1 ms, faster than 100.00% of Java online submissions for Lemonade Change.
Memory Usage: 39.9 MB, less than 99.24% of Java online submissions for Lemonade Change.

*/