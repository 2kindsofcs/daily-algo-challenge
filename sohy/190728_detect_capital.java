class Solution {
    public boolean detectCapitalUse(String word) {
        
        char[] charWord = word.toCharArray();
        int numOfCapital = 0; 
        for (char eachWord: charWord) {
            if (Character.isUpperCase(eachWord)) numOfCapital ++; 
        }
        
        if (numOfCapital == 0) return true;
        else if (numOfCapital == 1 && Character.isUpperCase(charWord[0])) return true; 
        else if (numOfCapital == word.length()) return true; 
        return false; 
    }
}

/*
Runtime: 1 ms, faster than 100.00% of Java online submissions for Detect Capital.
Memory Usage: 34.8 MB, less than 100.00% of Java online submissions for Detect Capital.

*/