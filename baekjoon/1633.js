const solution = (arr)=>{
    const dp = Array.from({length:16},()=> Array.from({length:16}).fill(0));
    for (const [white,black] of arr){
        for (let w_idx = 15; w_idx >= 0; w_idx--) {
            for (let b_idx = 15; b_idx >= 0; b_idx--) {
                if (w_idx > 0) {
                    dp[w_idx][b_idx] = Math.max(dp[w_idx][b_idx], dp[w_idx - 1][b_idx] + white);
                }
                if (b_idx > 0) {
                    dp[w_idx][b_idx] = Math.max(dp[w_idx][b_idx], dp[w_idx][b_idx - 1] + black);
                }
            }
        }
    }
    return dp[15][15];
}
// 입력
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const arr = new Array();
rl.on('line', (line) => {
    if (line === '') rl.close();
    arr.push(line.split(' ').map(Number));

});
rl.on('close', () => {
  const ans = solution(arr);
  console.log(ans);
});