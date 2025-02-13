const solution = (N)=>{
    return Math.floor(Math.sqrt(N))
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let N;
rl.on('line',(line)=>{
    N = parseInt(line)
    rl.close();
})

rl.on('close',()=>{
    const ans = solution(N);
    console.log(ans)
})