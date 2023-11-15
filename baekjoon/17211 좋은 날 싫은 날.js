// 좋은날 = 0, 싫은 날 = 1
const fs = require('fs');
const inputUrl = process.platform == 'linux' ? 'dev/stdin' : './17211.txt';
const inputs = fs.readFileSync(inputUrl).toString().trim().split('\n');
const [N,mood] = inputs[0].split(' ').map(Number);
const per = inputs[1].split(' ').map(Number);
const persent = [
    [per[0],per[1]],
    [per[2],per[3]]
];

let moods = new Array(2);
moods[0] = [(1-mood)*100,mood*100];

for (let i=0; i <N; i++){
    const beforeGoodMood = moods[i%2][0];
    const beforeBadMood = moods[i%2][1];
    const afterGoodMood = beforeGoodMood * persent[0][0] + beforeBadMood*persent[1][0];
    const afterBadMood = beforeGoodMood * persent[0][1] + beforeBadMood*persent[1][1];
    moods[(i+1)%2] = [afterGoodMood,afterBadMood]
};
const answer = moods[N%2]
for (let ans of answer){
    console.log(Math.round(ans*10));
};

