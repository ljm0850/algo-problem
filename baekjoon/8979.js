const solution = (N,K,arr) =>{
    arr.sort((a,b)=>{
        if (a[1] !== b[1]) return b[1] - a[1];
        if (a[2] !== b[2]) return b[2] - a[2];
        return b[3] - a[3];
    })
    for (let rank=0; rank<=N;rank++){
        const [idx,gold,silver,bronze] = arr[rank];
        if (idx === K){
            for (let totalRank=rank-1;totalRank>=0;totalRank--){
                const data = arr[totalRank];
                if (gold === data[1] && silver === data[2] && bronze === data[3]) continue
                else return totalRank+2
            }
            return 1
        }
    }
}

// 입력
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let [original_N,N,K] = [-1,-1,-1];
let arr;

rl.on('line', (line)=>{
    if (N==-1){
        [N,K] = line.split(' ').map(Number);
        original_N = N;
        arr = Array.from({length:N+1});
    } else if(N == 0){
        rl.close();
    } else {
        N --;
        const [i,gold,silver,bronze] = line.split(' ').map(Number);
        arr[i] = [i,gold,silver,bronze];
    }
});
rl.on('close',()=>{
   const ans = solution(original_N,K,arr)
   console.log(ans)
})