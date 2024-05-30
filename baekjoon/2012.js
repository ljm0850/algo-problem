const fs = require('fs');
const URI = process.platform === 'linux'? 0:'./2012.txt';
const [N,...arr] = fs.readFileSync(URI,'utf-8').toString().trim().split('\n').map(Number);
arr.sort((a,b)=>a-b);
let answer = 0;
arr.forEach((value,idx)=>{
    answer += Math.abs(idx+1-value);
})
console.log(answer);