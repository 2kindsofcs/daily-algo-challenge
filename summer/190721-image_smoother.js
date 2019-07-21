const smooth = M=>{
	const result = [];
	const _range = (v, x, y)=>{
		const result = [];
		[y-1, y, y+1].forEach(currY=>{
			if(v[currY] != undefined){
				[x-1, x, x+1].forEach(currX=>{
					if(v[currY][currX] !== undefined) result.push(v[currY][currX]);
				});
			}
		});
		return result;
	};
	M.map((row, y)=>{
		row.forEach((v, x)=>{
			if(x == 0) result.push([]);
			const neighbors = _range(M, x, y);
			result[y][x] = Math.floor(neighbors.reduce((p,c)=>p+c, 0) / neighbors.length);
		});
	});
	return result;
};