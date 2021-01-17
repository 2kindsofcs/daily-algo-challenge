func isValid(s string) bool {
    dic := make(map[rune]rune)
    dic['('] = ')'
    dic['{'] ='}'
    dic['['] = ']'
    stack := make([]rune, 0)
    stack = append(stack, []rune(s)[0])
    
    for _, char := range s[1:] {
        if _, ok := dic[char]; ok {
            stack = append(stack, char)
            continue 
        }
        prev := pop(&stack)
        if dic[prev] != char {
            return false
        }
    }
    if len(stack) == 0 {
        return true
    }
    return false
}

func pop(runes *[]rune) rune {
    length := len(*runes)
    if length == 0 {
        return 0
    }
    list := *runes
    if length == 1 {
        res := list[0]
        *runes = make([]rune, 0)
        return res
    }
    res := list[length-1]
    *runes = list[0:length-1]
    return res
}

// https://leetcode.com/problems/valid-parentheses/
