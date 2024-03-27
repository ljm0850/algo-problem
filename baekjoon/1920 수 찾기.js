const fs = require('fs');
const URI = process.platform === 'linux'? 'dev/stdin':'./1920.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n');
const N = inputs.shift();
const nums = new Set(inputs.shift().split(' '));
const M = inputs.shift();
const target = inputs.shift().split(' ');
answer = [];
for (let i = 0; i<M; i++){
    answer.push(nums.has(target[i]) === true?1:0)
}
console.log(answer.join('\n'));