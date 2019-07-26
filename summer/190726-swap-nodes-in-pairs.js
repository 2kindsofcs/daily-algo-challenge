/*
class ListNode{
	constructor(val){
		this.val = val;
		this.next = null;
	}
}; */
const swapPairs = head=>{
    if(!head || !head.next) return head;
    const next = head.next;
    head.next = swapPairs(next.next);
    next.next = head;
    return next;
};