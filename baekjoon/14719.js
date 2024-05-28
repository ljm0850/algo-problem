const fs = require('fs');
const URI = process.platform === 'linux'? 0:'./14719.txt';
const input = fs.readFileSync(URI,'utf-8').toString().trim().split('\n');
const [H,W] = input.shift().split(' ').map(Number);
const blocks = input.shift().split(' ').map(Number);

function solution(H,W,blocks){
    function makeMap(H,W,blocks){
        const arr = Array.from({length:H},()=>new Array(W).fill(0));
        for (let c=0; c<W; c++){
            for (let r=0; r<blocks[c]; r++){
                arr[r][c] = 1;
            };
        };
        return arr;
    }
    function checkMap(rows,cols,arr){
        let value = 0;
        for (let r=0; r<rows; r++){
            let beforeCol = -1;
            for (let c=0; c<cols; c++){
                if (arr[r][c]===1){
                    if (beforeCol !== -1){
                        value += c - beforeCol -1;
                        beforeCol = c;
                    } else {
                        beforeCol = c;
                    };
                };
            };
        };
        return value;
    };
    const arr = makeMap(H,W,blocks);
    const ans = checkMap(H,W,arr);
    return ans;
}
const answer = solution(H,W,blocks);
console.log(answer);