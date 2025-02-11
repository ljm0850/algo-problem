const solution = (N,L,arr)=>{
    let record = arr[0]+L;
    let cnt = 1;
    for (const num of arr){
        if ( record>num) continue
        cnt ++;
        record = num+L
    }
    return cnt
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let N,L;
let arr;
rl.on('line',(line)=>{
    if (N === undefined){
        [N,L] = line.split(' ').map(Number);
    } else {
        arr = line.split(' ').map(Number).sort((a,b)=>a-b)
        rl.close();
    }
})

rl.on('close',()=>{
    const ans = solution(N,L,arr)
    console.log(ans)
})