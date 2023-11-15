function solution(money) {
    const M = money.length;
    const cnt = (dp,money,idx,I,)=>{
        for (let i=idx; i<I; i++){
            dp[i] = Math.max(dp[i-2] + money[i],dp[i-1]);
        };  
    };
    const dp1 = new Array(M).fill(0);    // 첫 집을 털었을때
    const dp2 = new Array(M).fill(0);    // 첫 집을 안털었을때
    dp1[0] = dp1[1] = money[0];  // 첫 집을 털었음
    dp2[1] = money[1];
    cnt(dp1,money,2,M-1);
    cnt(dp2,money,2,M);
    return Math.max(dp1[M-2],dp2[M-1]);
}