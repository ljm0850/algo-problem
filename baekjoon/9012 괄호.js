const fs = require('fs');
const URI = process.platform ==='linux'? 'dev/stdin':'./9012.txt';
const inputs = fs.readFileSync(URI).toString().trim().split('\n');
tc = Number(inputs[0])
for (let i = 1; i<=tc; i++){
    const target = inputs[i];
    const stack = [];
    let flag = true;
    for (let idx = 0; idx<target.length; idx++){
        if (target[idx] === '('){stack.push(true)}
        else if (stack.length === 0){
            flag = false;
            break;
        }
        else {stack.pop()}
    }
    if (flag === true && stack.length === 0 ) {console.log('YES')}
    else {console.log('NO')}
}