const solution = (R,C,Q,data)=>{
    const command = data.slice(R);
    const arr = Array.from({length:R+1},()=>Array.from({length:C+1}).fill(0));
    const answer = [];
    for (let r=1;r<=R;r++){
        for (let c=1;c<=C;c++){
            arr[r][c] = arr[r-1][c] + arr[r][c-1] -arr[r-1][c-1] + data[r-1][c-1]
        }
    }
    for (const [r1,c1,r2,c2] of command){
        const total = arr[r2][c2] - arr[r2][c1-1] - arr[r1-1][c2] + arr[r1-1][c1-1];
        answer.push(Math.trunc(total/((r2-r1+1)*(c2-c1+1))))
    }
    return answer
}

const fs = require('fs');
const URI = process.platform === 'linux'?0:'./16507.txt';
const [[R,C,Q],...inputs] = fs.readFileSync(URI,'utf-8').toString().trim().split('\n').map(str=> {return str.split(' ').map(Number)});
const ans = solution(R,C,Q,inputs)
ans.forEach((value)=>console.log(value))