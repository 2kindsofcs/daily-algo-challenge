import java.util.HashMap;

// import java.util.regex.*;

class Solution {
    
    public boolean canConstruct(String ransomNote, String magazine) {
            
        HashMap<Character, Integer> hashmap = new HashMap<>();
        for (char str: magazine.toCharArray()) {
            if (hashmap.containsKey(str)) {
                hashmap.put(str, hashmap.get(str)+1);
            } else {
                hashmap.put(str, 1);
            }
        }

        for (char ransom: ransomNote.toCharArray()) {
            if (hashmap.containsKey(ransom)) {
                if (hashmap.get(ransom) <= 0) {
                    return false;
                } else {
                    hashmap.put(ransom, hashmap.get(ransom)-1);
                }
            } else {
                return false;
            }
        }
        return true;
            
        
    }
} 


/*
Runtime: 26 ms, faster than 19.02% of Java online submissions for Ransom Note.
Memory Usage: 37.7 MB, less than 99.60% of Java online submissions for Ransom Note.

** approched with regex -> read, clearify the question. regex involves ordering while this question doesnt 
        /*
        String pattern = ".*";
        char[] ransomNoteArr = ransomNote.toCharArray();
        for (char eachChar: ransomNoteArr) {
            pattern += "[" + eachChar + "]";
            pattern += ".*";
        }
        
        if (Pattern.matches(pattern,magazine)) return true; 
        return false; 
        */ 
 
*/