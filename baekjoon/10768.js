function solution(month,day,specialMonth,specialDay){
    if (month > specialMonth){
        return "After";
    } else if (month < specialMonth){
        return "Before";
    }
    if (day > specialDay){
        return "After";
    } else if (day < specialDay){
        return "Before";
    } else {
        return "Special";
    }

}

const fs = require('fs');
const URI = process.platform === 'linux'? 0:'./10768.txt';
const [month,day] = fs.readFileSync(URI,'utf-8').toString().trim().split('\n').map(Number);
const specialMonth = 2;
const specialDay = 18;
const ans = solution(month,day,specialMonth,specialDay);
console.log(ans);