const fs = require("fs");
const URI = process.platform ==='linux'? 'dev/stdin':'./20126.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n').map(x=>x.split(' ').map(Number));

const solution = (N,M,S,arr)=>{
    arr.sort((a,b)=>a[0]-b[0]);
    let nowTime = 0;
    for (let idx=0; idx<=N; idx++){
        const [startTime,duration] = arr[idx];
        if (startTime-nowTime >=M)return nowTime;
        nowTime = startTime+duration;
    }
    if (S-nowTime >= M)return nowTime;
    return -1;
}

const [N,M,S] = inputs[0];
const testArray = Array.from({length:N+1}, ()=> new Array(2).fill(0));

for (let i = 1; i<=N; i++){
    testArray[i] = inputs[i];
}
const ans = solution(N,M,S,testArray);
console.log(ans);