const fs = require("fs");
const inputUrl = process.platform === 'linux' ? 'dev/stdin' : './10813.txt';
const inputs = fs.readFileSync(inputUrl).toString().trim().split('\n');
const T = inputs[0].split(' ').map(Number);
const N = T[0], M = T[1];
let bucket = Array.from({ length: N+1 }, (_, idx) => idx);

const swapIdx = (arr,a,b)=>{
    if (a===b){
        return
    }
    arr[a] = arr[a] ^ arr[b];
    arr[b] = arr[a] ^ arr[b];
    arr[a] = arr[a] ^ arr[b];
}

for (let idx = 1; idx<=M; idx++){
    const value = inputs[idx].split(' ').map(Number)
    const i = value[0], j = value[1];
    swapIdx(bucket,i,j)
}
let ans = ''
for (let i=1; i<=N; i++){
    ans += bucket[i] + ' '
}
console.log(ans.trimEnd());