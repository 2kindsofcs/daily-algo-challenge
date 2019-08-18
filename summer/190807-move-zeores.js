/* 문제
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

ex 1.
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

ex 2.
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

ex 3.
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


*/
/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
const isAlienSorted = (words, order)=>{
	let curr, isSorted = true, len = words.length;
	if(!len || len > 100 || !order) return false;
	const _getOrder = v=>v?order.indexOf(v):-1;	
	while(curr = words.shift()){
		if(!isSorted) break;
		words.some(word=>{
			let i = 0 ;
			while(i < curr.length){
				const letterToCompare = word[i];
				const currOrder = _getOrder(curr[i]);
				const comparingOrder = _getOrder(letterToCompare);
				if(!letterToCompare || currOrder > comparingOrder){
					isSorted = false;
					return true;
				}else if(currOrder == comparingOrder) i++;
				else return true;
			}
		});
	}	
	return isSorted;
};