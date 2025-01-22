const solution = (N,graph)=>{
    const visit = Array.from({length:N}).fill(false);
    const recur = (node,deepth)=>{
        if (deepth === 5) return true;
        for (const next_node of graph[node]){
            if (visit[next_node] === true) continue;
            visit[next_node] = true;
            const value = recur(next_node,deepth+1)
            visit[next_node] = false;

            if (value === true) return true;
        }
        return false;
    }

    for (let node=0; node<N; node++){
        visit[node] = true;
        if (recur(node,1)) return true;
        visit[node] = false;
    }
    return false;
}

let graph;
let [N,M] = [null,null]
// 입력
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
rl.on('line', (line)=>{
    if (N===null){
        [N,M] = line.split(' ').map(Number);
        graph = Array.from({length:N},()=>new Set());
    } else if (M===0) {
        rl.close();
    } else {
        M --;
        const [a,b] = line.split(' ').map(Number);
        graph[a].add(b)
        graph[b].add(a)
    }
});
rl.on('close',()=>{
    const ans = solution(N,graph);
    if (ans === true) console.log(1);
    else console.log(0);
})