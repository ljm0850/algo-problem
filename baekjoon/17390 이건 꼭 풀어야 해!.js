const fs = require('fs');
const URI = process.platform === 'linux'? 'dev/stdin':'./17390.txt';
const [first,arr,...datas] = fs.readFileSync(URI).toString().trim().split('\n').map((x)=>x.split(' ').map(Number));
const [N,Q] = first;
arr.sort((a,b)=> a-b);
const sumArr = new Array(N+1).fill(0);
let total = 0;
for (let i=1; i<=N; i++){
    total += arr[i-1];
    sumArr[i]= total;
};
answer = new Array()
for (let i=0; i<Q; i++){
    const [L,R] = datas[i]
    answer.push(sumArr[R]-sumArr[L-1])
};
console.log(answer.join('\n'))