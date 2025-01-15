const solution = (commands)=>{
    const positionSet = (commands)=>{
        let [minRow,maxRow,minColumn,maxColumn] = [51,51,51,51];
        const dr = [1,0,-1,0];
        const dc = [0,-1,0,1];
        let [r,c,d] = [51,51,0];
        const position = new Set([51051]);
        for (const commnad of commands){
            switch (commnad) {
                case 'F':
                    [r,c] = [r+dr[d],c+dc[d]];
                    position.add(r*1000+c)
                    switch (d){
                        case 0:
                            maxRow = Math.max(maxRow,r);
                            break;
                        case 1:
                            minColumn = Math.min(minColumn,c);
                            break;
                        case 2:
                            minRow = Math.min(minRow,r);
                            break;
                        case 3:
                            maxColumn = Math.max(maxColumn,c);
                            break
                    };
                    break;
                case 'R':
                    d = (d+1)%4;
                    break;
                case 'L':
                    d = (d+3)%4;
                    break;
            };
        }
        return [minRow,maxRow,minColumn,maxColumn,position];
    }
    const [minRow,maxRow,minColumn,maxColumn,position] = positionSet(commands);
    const [R,C] = [maxRow-minRow+1,maxColumn-minColumn+1];
    const arr = Array.from({length:R},()=>Array.from({length:C}).fill('#'));
    for (const num of position){
        const [r,c] = [Math.floor(num/1000)-minRow,num%1000-minColumn];
        arr[r][c] = '.';
    }
    return arr;
}

const fs = require("fs");
const URI = process.platform === 'linux'? 0:'./1347.txt';
const [C,commands] = fs.readFileSync(URI,'utf-8').toString().trim().split('\n');
const ans = solution(commands)
ans.forEach((arr)=>console.log(arr.join('')));