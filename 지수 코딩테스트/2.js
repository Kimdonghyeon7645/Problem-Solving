function solution(foods) {
    let result = 0,
        n = foods.length;
    let sumX = 0;
    for (let x = 0; x < n-2; x++) {
        sumX += foods[x];
        console.log("x : ", sumX);
        let sumY = 0,
            sumN = foods.slice(x+1, n).reduce((a, b) => a+b);
        if (sumN != sumX * 2)   continue;
        for (let y = x+1; y < n-1; y++) {
            sumY += foods[y];
            sumN -= foods[y];
            console.log("== y : ", sumY, " / z : ", sumN);
            if (sumX == sumY && sumY == sumN)   result++;
        }
    }
    return result;
}

console.log(solution([1, 2, 3, 0, 3]));
console.log(solution([4, 1]));
console.log(solution([1, 3, -2, 2, -1, 3]));
