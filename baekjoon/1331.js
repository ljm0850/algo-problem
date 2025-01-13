const solution = (size,array)=>{
    const transPosition = (alpha,number)=>{return [alpha.charCodeAt()-65,Number(number)-1]};
    const check = (r1,c1,r2,c2) => {
        const [gap1,gap2] = [Math.abs(r1-r2),Math.abs(c1-c2)]
        if (gap1>=3||gap2>=3||gap1+gap2 !== 3){return false};
        return true;
    };
    const visit = Array.from({length:6},()=> Array.from({length:6}).fill(0))
    let [br,bc] = transPosition(...array[size*size-1]);
    for (position of array){
        const [r,c] = transPosition(...position);
        if (visit[r][c]===1 || check(br,bc,r,c)===false) {return false};
        visit[r][c] = 1;
        [br,bc] = [r,c];
    }
    return true;
}

const fs = require('fs');
const URI = process.platform === 'linux'? 0:'./1331.txt';
const inputs = fs.readFileSync(URI,'utf-8').toString().trim().split('\n');
const size = 6
const ans = solution(size,inputs)
if (ans===true){console.log("Valid")}
else {console.log("Invalid")}