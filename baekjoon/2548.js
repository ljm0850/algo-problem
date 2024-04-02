const fs = require('fs');
const URI = process.platform === 'linux'?'dev/stdin':'./2548.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n');
const N = Number(inputs.shift());
const nums = inputs.shift().split(' ').map(Number);
nums.sort((a,b)=>(a-b));
const mid = N%2===1?Math.floor(N/2):Math.floor(N/2)-1;
console.log(nums[mid]);