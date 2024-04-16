const solution = (N,M,vips) =>{
    const dp = new Array(N+1).fill(1);
    for (let idx = 2; idx<=N; idx++){
        dp[idx] = dp[idx-1] + dp[idx-2];
    }
    let answer = 1;
    let vipIdx = 0;
    for (let i=0; i<M; i++){
        const vip = vips[i];
        answer *= dp[vip-vipIdx-1];
        vipIdx = vip;
    }
    answer *= dp[N-vipIdx];
    return answer;
}

const fs = require("fs");
const URI = process.platform === "linux"?"dev/stdin":"./2302.txt";
const inputs = fs.readFileSync(URI).toString().trim().split('\n').map(Number);
const N = inputs.shift();
const M = inputs.shift();
const vips = inputs;
const ans = solution(N,M,vips);
console.log(ans);