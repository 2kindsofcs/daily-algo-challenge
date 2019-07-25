class Solution {
    public boolean rotateString(String A, String B) {
        int lenA = A.length();
        int lenB = B.length();
        if (lenA != lenB) {
            return false; 
        } else if (lenA == 0 && lenB == 0) {
            return true; 
        }
        
        
        int count = 0; 
        while (count < lenA) {
            char current = A.charAt(0);
            A = A.substring(1) + current; 
            System.out.println(A);
            if (A.equals(B)) {
                return true; 
            }
            count ++; 
        }
        return false; 
        
    }
}

/*
Runtime: 8 ms, faster than 5.12% of Java online submissions for Rotate String.
Memory Usage: 36.1 MB, less than 34.32% of Java online submissions for Rotate String.

-> need to optimize 

*/ 