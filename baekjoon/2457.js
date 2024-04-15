const solution = (arr)=>{
    arr.sort((a,b) => a[0]-b[0]);
    let cnt = 1;
    let start,end;
    let nextStart,nextEnd;

    for (let i = 0; i<arr.length; i++){
        const s = arr[i][0];
        const e = arr[i][1];

        if (s > 1131) break;    // 11월 30일 이후에 피는 꽃
        else if ( nextEnd >= e || e <= 301) continue;   // 필요없는 값
        else if (s > nextEnd) break;   // 중간에 빈 기간이 있는 경우
        

        if (start === undefined){
            if (s > 301) {
                end = -1;
                break
            }
            start = s;
            end = e;
        }
        else if (nextStart === undefined){
            if (s <= 301 && end<e){
                start = s;
                end = e;
            } else if (end < s){
                break;
            } else if (end < e) {
                nextStart = s;
                nextEnd = e;
            } else continue;
        }

        // 기존 넥스트가 필요 없을 경우
        else if (start <= s && s <= end) {
            nextStart = s;
            nextEnd = e;
        } 
        // 다음 값이 갱신되야 할 경우
        else {
            start = nextStart;
            end = nextEnd;
            nextStart = s;
            nextEnd = e;
            cnt ++;
        }
    }
    if (end <= 1131 && nextEnd !== undefined) {
        end = nextEnd;
        cnt ++;
    }
    
    if (end <= 1131) return 0;
    return cnt;

}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let N = -1;
const arr = new Array();

rl.on("line",(line)=>{
    if (N === -1) N = parseInt(line);
    else if (N > 0){
        const day = line.split(' ').map(Number);
        arr.push([day[0]*100+day[1],day[2]*100+day[3]])
        N --;
    }
    else rl.close();
}).on("close",()=>{
    const ans = solution(arr);
    console.log(ans);
})