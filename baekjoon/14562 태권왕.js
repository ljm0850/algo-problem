const fs = require("fs");
const URI = process.platform == 'linux' ? 'dev/stdin' : './14562.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n');
const C = Number(inputs[0]);

const solution = (S,T)=>{
    const arr = [[S,T,0]];
    while (arr.length){
        const [value,end,cnt] = arr.shift();
        const v1 = value+1, v2 = 2*value;
        if (v1 === end| v2 === end+3 ){
            return cnt + 1;
        };
        if (v1 < end){
            arr.push([v1,end,cnt+1]);
        };
        if (v2 < end+3){
            arr.push([v2,end+3,cnt+1]);
        };
    }
    return 0;
}

for (let i=1; i <= C; i++){
    const [S,T] = inputs[i].split(' ').map(Number);
    ans = solution(S,T);
    console.log(ans);
};