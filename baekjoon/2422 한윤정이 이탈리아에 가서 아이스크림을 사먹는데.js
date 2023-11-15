const fs = require('fs');
const URI = process.platform ==='linux' ? 'dev/stdin' : './2422.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n');
const [N,M] = inputs[0].split(' ').map(Number);
let total = N*(N-1)*(N-2)/6;
let badComb = new Set();
for (let idx=1; idx<=M; idx++){
    const [a,b] = inputs[idx].split(' ').map(Number);
    for (let num=1; num<=N; num++){
        if (num !== a && num !== b){
            const value = [a,b,num];
            value.sort();
            badComb.add(value.toString());
        };
    };
};
console.log(total-badComb.size);
// badcomb 를 2중 배열로 만든 후 badcomb[i][j] 에 true, false 를 설정하고
// 3개의 숫자를 N까지 반복하여 badcomb[i][j]에 그 숫자가 있는지 확인하는 방식이 정석