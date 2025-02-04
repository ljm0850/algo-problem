// logic
const solution = (M,N,arr)=>{
    arr.sort((a,b)=>b-a)
    let [s,e] = [0,1000000000];
    let ans = 0;
    while (s<=e) {
        let cnt = 0;
        const mid = Math.floor((s+e)/2);
        for (const len of arr)cnt += Math.floor((len)/mid);
        if (cnt>=M) {
            ans = mid;
            s = mid+1;
        } else e = mid-1;
    }
    return ans;
}

// IO
let M,N,arr;
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line',(line)=>{
    M===undefined? [M,N] = line.split(' ').map(Number): arr = line.split(' ').map(Number);
    if (arr !== undefined) rl.close();
});
rl.on('close',()=>{
    const ans = solution(M,N,arr);
    console.log(ans);
});