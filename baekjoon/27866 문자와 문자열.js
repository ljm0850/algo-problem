const fs = require("fs");
const file = process.platform === 'linux' ? 'dev/stdin' : './27866.txt'
const inputs = fs.readFileSync(file).toString().trim().split('\n');
let voca = inputs[0].toString();
let num = Number(inputs[1]);
console.log(voca[num-1])