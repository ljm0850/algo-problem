// 함수
function solution(D,N,oven,pizza){
    const [minArray,cnt] = minCheck(oven)
    for (const length of pizza){
        while (minArray.length !== 0){
            if (length > minArray[minArray.length-1]){
                const num = minArray.pop();
                delete cnt[num];
            } else break;
        }
        if (minArray.length !== 0){
            const ovenSize = minArray.at(-1);
            cnt[ovenSize] -= 1
            if (cnt[ovenSize]===0){
                minArray.pop();
                delete cnt[ovenSize];
            }
        } else return 0;
    }
    let answer = 1;
    for (const size of minArray){
        answer += cnt[size];
    }
    return answer;
}
function minCheck(arr){
    const value = new Array();
    const cnt = new Object();
    let minValue = 1000000001
    for (const num of arr){
        if (num < minValue){
            minValue = num
            value.push(minValue)
            cnt[minValue] = 1
        } else cnt[minValue] += 1
    }
    return [value,cnt]
}
// 인풋
const fs = require('fs');
const URI = process.platform === 'linux'? 0:'./1756.txt';
const inputs = fs.readFileSync(URI,'utf-8').toString().trim().split('\n');
const pizza = inputs.pop().split(' ').map(Number);
const oven = inputs.pop().split(' ').map(Number);
const [D,N] = inputs.pop().split(' ').map(Number);
// 실행
const ans = solution(D,N,oven,pizza);
console.log(ans)