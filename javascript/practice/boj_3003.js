let fs = require('fs')
let input = fs.readFileSync('input.txt').toString().split(' ')
input.map(parseInt) // 이렇게 따로 해줘야함. 한줄에 같이하면 .split()은 원본을 변경하기 때문.
let arr = [1,1,2,2,2,8]
let ans = []
for (i=0;i<6;i++){
  ans.push(arr[i]-parseInt(input[i]))
}
console.log(ans.join(' '))