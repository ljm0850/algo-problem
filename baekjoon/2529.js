const solution = (k,condition)=>{
    const ascNumber = [0,1,2,3,4,5,6,7,8,9];
    const descNumber = [9,8,7,6,5,4,3,2,1,0];
    let maxValue;
    for (let num = 9; num>-1; num --){
        visit[num] = true;
        const value = recur(k,descNumber,0,condition,String(num));
        visit[num] = false;
        if (value !== '') {
            maxValue = value;
            break;
        }
    }
    let minValue;
    for (let num = 0; num < 10; num ++){
        visit[num] = true;
        const value = recur(k,ascNumber,0,condition,String(num));
        visit[num] = false;
        if (value !== ''){
            minValue = value;
            break;
        }
    }
    return `${maxValue}\n${minValue}`
}

const recur = (k,arr,idx,condition,total)=>{
    if (idx === k) return total
    for (let i = 0; i < 10; i++){
        const num = arr[i];
        if (visit[num]) continue
        const lastNum = Number(total[total.length-1])
        if (condition[idx] === '<'){
            if (lastNum < num) {
                visit[num] = true;
                const value = recur(k,arr,idx+1,condition,total+String(num))
                visit[num] = false;
                if (value !== '') return value
            }
        } else {
            if (lastNum > num) {
                visit[num] = true;
                const value = recur(k,arr,idx+1,condition,total+String(num))
                visit[num] = false;
                if (value !== '') return value
            
            }
        }
    }
    return ''
}

const fs = require('fs');
const URI = process.platform === 'linux'? 0:'./2529.txt';
const inputs = fs.readFileSync(URI,'utf-8').toString().trim().split('\n');
const k = Number(inputs.shift());
const condition = inputs.shift().trim().split(' ');
const visit = new Array(10).fill(false);
const ans = solution(k,condition);
console.log(ans);