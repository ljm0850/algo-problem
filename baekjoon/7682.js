function check(ticTacToe){
    const row = 3;
    const col = 3;
    const arr = Array.from({length:row}).fill("");
    for (let i = 0; i<3; i++){
        arr[i] = ticTacToe.slice(3*i,3*i+3)
    };

    // O,X 개수 체크
    let flag = false;
    let cnt = 0
    for (let r = 0; r<row; r++){
        for (let c = 0; c<col; c++){
            if (arr[r][c] === 'X') cnt ++
            else if (arr[r][c] === 'O') cnt --
            else flag = true;
        }
    }
    if (!(cnt===0 || cnt===1 )) return false;

    // 완성 체크
    // 가로
    let oCnt = 0;
    let xCnt = 0;
    const bingo = new Set();
    for (let r = 0; r<row; r++){
        if (arr[r]==='OOO'){
            oCnt ++;
            for (let c=0; c<col; c++) bingo.add(3*r+c);
        } else if (arr[r]==='XXX'){
            xCnt ++
            for (let c=0; c<col; c++) bingo.add(3*r+c);
        };
    }
    // 세로
    for (let c = 0; c<col; c++){
        if (arr[0][c] === 'O' && arr[1][c] === 'O' && arr[2][c] === 'O'){
            oCnt ++;
            for (let r = 0; r<row; r++) bingo.add(3*r+c);
        }
        else if (arr[0][c] === 'X' && arr[1][c] === 'X' && arr[2][c] === 'X') {
            xCnt ++;
            for (let r = 0; r<row; r++) bingo.add(3*r+c);
        }
    }
    // 대각선
    if (arr[1][1] === 'O'){
        if (arr[0][0] === 'O' && arr[2][2] === 'O') {
            oCnt ++;
            for (let i=0; i<3; i++) bingo.add(4*i);
        } else if (arr[2][0] === 'O' && arr[0][2] === 'O') {
            oCnt ++;
            for (let i=0; i<3; i++) bingo.add(6-2*i);
        };
    } else if (arr[1][1] === 'X'){
        if (arr[0][0] === 'X' && arr[2][2] === 'X') {
            xCnt ++;
            for (let i=0; i<3; i++) bingo.add(4*i);
        } else if (arr[2][0] === 'X' && arr[0][2] === 'X') {
            xCnt ++;
            for (let i=0; i<3; i++) bingo.add(6-2*i);
        }
    }

    if (oCnt >=1 && xCnt >=1) return false; // ox 둘 다 완성됨
    else if ((oCnt === 2 || xCnt === 2) && bingo.length === 6 ) return false; // 겹치는 곳이 없는데 2줄이 완성 될 수 없음
    if (oCnt >=1 && cnt === 1) return false; // o가 완성돴는데 x를 둠
    if (xCnt >=1 && cnt === 0) return false; // x가 완성됬는데 o를 둠
    if (flag && xCnt === 0 && oCnt === 0) return false; // 완성이 없는데 중간에 멈춘 경우
    return true;
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let ans = ""
rl.on("line",(line)=>{
    const result = line
    if (result !== "end"){
        const value = check(line);
        if (value) ans += "valid\n";
        else ans += "invalid\n";
    }
    else rl.close();
}).on("close",()=>{
    console.log(ans);
})