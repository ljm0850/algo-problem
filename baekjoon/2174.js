// input
const fs = require('fs');
const URI = process.platform === 'linux'? 0:'./2174.txt';
const [mapSize,robotCnt,...inputs] = fs.readFileSync(URI,'utf-8').toString().trim().split('\n');
const [cols,rows] = mapSize.split(' ').map(Number);
const [N,M] = robotCnt.split(' ').map(Number);
const positionData = inputs.slice(0,N);
const cmdData = inputs.slice(N);

function solution(positionData,cmdData,N,M,cols,rows){
    // 로봇 위치, 방향 설정
    function defineRobotPosition(positionData,rows,cols){
        const arr = Array.from({length:rows+1}, ()=> new Array(cols+1).fill(0));
        const robotPosition = {};
        const robotDirection = new Array(N+1).fill(0);
        const conversionDirectionToNumber = { 'N':0, 'E':1,'S':2,'W':3 };
        for (let i = 0; i<positionData.length ;i++){
            const [c,r,d] = positionData[i].split(' ').map((value,idx)=> idx<2? Number(value):value);
            const robotId = i+1;
            arr[r][c] = robotId;
            robotPosition[robotId] = [r,c];
            robotDirection[robotId] = conversionDirectionToNumber[d];
        }
        return [arr,robotDirection,robotPosition];
    }
    // 범위 밖 나가는지 확인
    function inrange(r,c,rows,cols){
        if (0<r && r <= rows && 0<c && c<= cols) return true;
        return false;
    }
    // 로봇 움직임
    function cmdOppertaion(robotId,cmd,cnt,rows,cols){
        const directionMove = [[1,0],[0,1],[-1,0],[0,-1]];
        if (cmd === 'R'){
            cnt %= 4;
            robotDirection[robotId] = (robotDirection[robotId] + cnt) % 4;
        } else if (cmd === 'L'){
            cnt %= 4;
            robotDirection[robotId] = (robotDirection[robotId] + 4 - cnt)%4;
        } else{
            const [originR,originC] = robotPosition[robotId];
            let r = originR;
            let c = originC
            const d = robotDirection[robotId];
            for (let _ = 0; _ < cnt;_++){
                const nr = r + directionMove[d][0];
                const nc = c + directionMove[d][1];
                if (!(inrange(nr,nc,rows,cols))) return 0
                if (arr[nr][nc] !==0) return arr[nr][nc]
                r = nr;
                c = nc;
            }
            arr[originR][originC] = 0;
            arr[r][c] = robotId;
            robotPosition[robotId] = [r,c];

        }

        return -1
    }

    const [arr,robotDirection,robotPosition] = defineRobotPosition(positionData,rows,cols);
    for (let i = 0; i<M; i++){
        const [robotId,cmd,cnt] = cmdData[i].split(' ').map((value,idx)=> idx !=1? Number(value):value);
        const result = cmdOppertaion(robotId,cmd,cnt,rows,cols);
        if (result === 0) return `Robot ${robotId} crashes into the wall`
        if (result >0 ) return `Robot ${robotId} crashes into robot ${result}`
    }
    return 'OK'
}

const ans = solution(positionData,cmdData,N,M,cols,rows);
console.log(ans);