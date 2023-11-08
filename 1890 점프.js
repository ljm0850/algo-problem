const fs = require('fs');
const URI = process.platform ==='linux'? 'dev/stdin':'./1890.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n').map((x)=>x.split(' ').map(Number));
const N = inputs.shift()[0];
const arr = inputs;
const inrange = (i,N)=>{
    if (0<=i && i<N)return true;
    return false;
};

const dfs = (r,c,N)=>{
    const v = arr[r][c];
    if (v==0){
        check[r][c] = BigInt(-1);
        return 0;
    };

    const nr = r+v, nc = c+v;
    let value = BigInt(0);
    if (inrange(nr,N)){
        if (check[nr][c]>=1) {value += BigInt(check[nr][c])}
        else if (check[nr][c]==0){value += BigInt(dfs(nr,c,N))};
    };
    if (inrange(nc,N)){
        if (check[r][nc]>=1) {value += BigInt(check[r][nc])}
        else if (check[r][nc]==0){value += BigInt(dfs(r,nc,N))};
    };
    if (value == 0) check[r][c] = BigInt(-1);
    else check[r][c] = value;
    return value;
}
const check = Array.from({ length: N }, () => new Array(N).fill(BigInt(0)));
check[N-1][N-1] = BigInt(1);
const ans = dfs(0,0,N);
if (ans == -1){console.log(0)} else {console.log(ans.toString())};