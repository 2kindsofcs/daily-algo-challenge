func twoSum(nums []int, target int) []int {
    dic := make(map[int]int)
    for idx, num := range nums {
        diff := target - num
        if _, ok := dic[diff]; ok {
            return []int{dic[diff], idx}
        } else {
            dic[num] = idx
        }
    }
    return make([]int,2,2)
}

// https://leetcode.com/problems/two-sum/
