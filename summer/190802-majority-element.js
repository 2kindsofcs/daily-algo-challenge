/* 문제

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

*/
/**
 * @param {number[]} nums
 * @return {number}
 */
const majorityElement = nums=>{
    let v;
	const len = nums.sort().length;
	while(nums.length){
		v = nums[0];
		if(nums.splice(0, nums.lastIndexOf(v) + 1).length > len / 2) break;
	}    
	return v;
};

// 다른 답안을 보니 정렬한 건 괜찮은데, 그 뒤에 while 돌릴 필요 없이 배열에서 중앙 인덱스의 값을 리턴하면 됨.
// 무조건 과반 이상을 차지할거니까- 무조건 배열 중앙에 위치하게 됨