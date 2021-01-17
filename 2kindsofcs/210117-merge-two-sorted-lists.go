/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    if l2 == nil {
        return l1
    }
    
    head := &ListNode{}
    prev := head
    
    for l1 != nil {
        if l1.Val <= l2.Val {
            prev.Next = l1
            l1 = l1.Next
        } else {
            prev.Next = l2
            l2 = l2.Next
        }
        prev = prev.Next
        if l2 == nil {
            prev.Next = l1
            return head.Next
        }
    }
    prev.Next = l2
    return head.Next
}


// https://leetcode.com/problems/merge-two-sorted-lists
