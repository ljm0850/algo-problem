const solution = (N,mod)=>{
    const dp = Array.from({length:2},()=>Array.from({length:3}).fill(1));
    for (let cnt=1;cnt<=N;cnt++){
        const [bi,ni] = [(cnt-1)%2,cnt%2];
        dp[ni][0] = (dp[bi].reduce((total,value)=>total+value,0))%mod;
        dp[ni][1] = (dp[bi][0] + dp[bi][2])%mod;
        dp[ni][2] = (dp[bi][0] + dp[bi][1])%mod;
    };
    return dp[N%2][0];
}

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let N;
const mod = 9901;
rl.on('line', (line) => {
    N = parseInt(line);
    rl.close();
});
rl.on('close', () => {
  const ans = solution(N,mod);
  console.log(ans);
});