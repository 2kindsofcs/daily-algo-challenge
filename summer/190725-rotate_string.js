const rotateString = (A, B)=>{
	if(A == B) return true;
	if(A.length !== B.length) return false;
	var res = false;
	B.split('').reduce((arr, curr, idx)=>{
		if(curr == A[0]) arr.push(idx);
		return arr;
	}, []).forEach(v=>{
		if(A == B.slice(v, B.length) + B.slice(0, v)) res = true;
	});
	return res;
};