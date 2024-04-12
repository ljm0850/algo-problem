const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const solution = (R,C,arr,hole)=>{
    const mod = 10**9 + 7;
    hole.add(C+1);
    arr[1][1] = 1;
    for (let c=1; c<=C; c++){
        for (let r = 1; r<=R; r++){
            if (hole.has(r*C+c)) {continue}
            if (c%2 === 1){
                arr[r][c] = (arr[r-1][c] + arr[r][c-1] + arr[r-1][c-1]) % mod;
            } else {
                arr[r][c] = (arr[r-1][c] + arr[r][c-1] + arr[r+1][c-1]) % mod;
            }
        }
    }
    return arr[R][C];
}

const check = new Array();
let R,C;
let K = -1;
const hole = new Set();

rl.on("line",(line)=>{
    if (K === -1){
        [R,C] = line.split(' ').map(Number);
    } else if (K === -2){
        K = Number(line);
        for (let i = 0; i<=R+1; i++){
            check.push(new Array(C+1).fill(0))
        }
    } else {
        const [r,c] = line.split(' ').map(Number);
        hole.add(r*C + c);
    }
    if (K === 0) rl.close();
    K --;
}).on("close",()=>{
    const ans = solution(R,C,check,hole);
    console.log(ans);
})