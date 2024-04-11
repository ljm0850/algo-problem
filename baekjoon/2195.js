const fs = require("fs");
const URI = process.platform === 'linux'?'dev/stdin':'./2195.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n');
const S = inputs.shift();
const P = inputs.shift();

let ans = 1;
let idx = 0;

for (let i = 0; i< P.length; i++){
    if (S.indexOf(P.slice(idx, i+1)) > -1) continue
    idx = i;
    ans ++;
}
console.log(ans);

// const alphaSet = new Set();
// for (let i = 0; i < S.length; i++){
//     for (let j = i+1; j <= S.length; j++){
//         alphaSet.add(S.slice(i,j));
//     }
// }

// let ans = 0;
// let idx = 0;
// while (idx < P.length){
//     let nextIdx = idx+1;
//     for (let end = idx+1; end <= P.length; end ++){
//         const temp = P.slice(idx,end);
//         if (alphaSet.has(temp)) nextIdx = end;
//         else break;
//     }
//     idx = nextIdx;
//     ans ++
// }
// console.log(ans);