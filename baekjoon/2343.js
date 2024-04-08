const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const solution = (M,nums) =>{
    let s = Math.max(...nums);
    let e = 10000 * 100000;
    let ans = s;
    while (s<=e){
        const m = Math.floor((s+e)/2);
        let cnt = 1;
        let total = 0;

        nums.forEach(num => {
            total += num;
            if (total> m){
                total = num;
                cnt ++;
            }
        });

        if (cnt > M){
            s = m + 1;
        } else {
            e = m - 1;
            ans = m;
        }
    }
    return ans;
}

let L = 1;
let N,M,nums;
rl.on("line",(line)=>{
    if (L === 1){
        [N,M] = line.split(' ').map(Number);
        L --;
    }else if (L === 0){
        nums = line.split(' ').map(Number);
        rl.close();
    }

}).on("close",()=>{
    const ans = solution(M,nums);
    console.log(ans);
})