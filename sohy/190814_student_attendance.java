
class Solution {
    public boolean checkRecord(String s) {
        if (s.matches(".*A.*A.*")) {
            return false; 
        }
        
        if (s.matches(".*LLL.*")) {
            return false; 
        }
        
        return true;
        
    }
}


/*
Runtime: 4 ms, faster than 8.44% of Java online submissions for Student Attendance Record I.
Memory Usage: 34.9 MB, less than 100.00% of Java online submissions for Student Attendance Record I.
*/