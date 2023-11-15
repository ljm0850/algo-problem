const fs = require("fs");
const file = process.platform === 'linux' ? 'dev/stdin' : './27964.txt'
const inputs = fs.readFileSync(file).toString().trim().split('\n');

const Toppings = inputs[1].split(' ')
let total = new Set();
for (let i = 0; i < Number(inputs[0]); i++){
    const topping = Toppings[i]
    const T = topping.length
    const lastAlpha = topping.slice(T-6,T)
    if (lastAlpha == 'Cheese'){
        total.add(topping)
    }
}
if (total.size >= 4){
    console.log('yummy')
}
else{
    console.log('sad')
}