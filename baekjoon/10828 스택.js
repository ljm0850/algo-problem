const fs = require('fs');
const URI = process.platform === 'linux'? 'dev/stdin':'./10828.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n')
const N = inputs[0];
const stack  = [];
const answer = [];
for (let i=1; i<=N; i++){
    const order = inputs[i];
    if (order === 'pop') answer.push(stack.length === 0? -1:stack.pop());
    else if (order === 'size')  answer.push(stack.length);
    else if (order === 'empty') answer.push(stack.length === 0? 1:0);
    else if (order === 'top') answer.push(stack.length === 0? -1 : stack[stack.length-1])
    else {
        const arr = order.split(' ');
        stack.push(arr[1])
    }
}
console.log(answer.join('\n'));