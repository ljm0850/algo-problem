const fs = require('fs');
const URI = process.platform === 'linux'?'dev/stdin':'./5545.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n');
const N = Number(inputs.shift());
const [A,B] = inputs.shift().split(' ').map(Number);
const C = Number(inputs.shift());
const arr = inputs.map(Number);

const solution = (N,A,B,C,arr)=>{
    const sortedArr = [...arr].sort((a,b)=>b-a);
    let totalCost = A;
    let totalEntropy = C;
    let value = totalEntropy / totalCost;
    for (let i = 0; i < N; i++){
        totalCost += B;
        totalEntropy += sortedArr[i];
        const tempValue = totalEntropy / totalCost;
        if (value < tempValue){
            value = tempValue;
        } else break;
    }
    return value;
}

const ans = solution(N,A,B,C,arr);
console.log(Math.floor(ans));