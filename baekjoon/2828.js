const fs = require("fs");
const inputs = process.platform === 'linux'?fs.readFileSync(0, 'utf-8').toString().trim().split('\n'):fs.readFileSync("./2828.txt").toString().trim().split('\n');
const [N,M] = inputs.shift().split(' ').map(Number);
const [J,...apple] = inputs.map(Number);
let start = 1;
let end = M;
let ans = 0;

for (let i = 0; i<J; i++){
    const position = apple[i];
    if (start <= position && position <=end) continue
    else if (start > position){
        const gap = start - position;
        start -= gap;
        end -= gap;
        ans += gap
    } else {
        const gap = position - end;
        start += gap;
        end += gap;
        ans += gap
    }
}
console.log(ans);