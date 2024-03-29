const fs = require('fs');
const URI = process.platform === 'linux'? 'dev/stdin':'./11663.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n').map((x)=>x.split(' ').map(Number));

const biSearch = (nums,value)=>{
    let [s,e] = [0,nums.length -1];
    let m;

    while (s<=e){
        m = Math.floor((s+e)/2);
        if (nums[m] < value) s = m+1;
        else if (nums[m] > value) e = m -1;
        else return m -1
    }
    return e
}

const [N,M] = inputs[0];
const nums = inputs[1];
nums.sort((a,b)=>(a-b))
const ans = new Array();
for (let i = 2; i< M+2; i ++){
    const [s,e] = inputs[i];
    const value = biSearch(nums,e+1)-biSearch(nums,s);
    ans.push(value)
}
console.log(ans.join('\n'))