'use strict'

const { maxHeaderSize } = require("http")

    /*
      전기버스
      - A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
      - 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
      - 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
      - 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
      <입력>
        [
          3,   => 최대한 이동할 수 있는 정류장 수
          10,  => 종점 정류장 번호
          5,   => 설치된 충전기의 개수
          [1, 3, 5, 7, 9]  => 충전기가 설치된 정류장 번호
        ]
    
      <출력>
        현재 아래 주어진 입력에 따른 출력은
          3
          0
          4
        이다.
    */

        const inputs = [
          [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
          [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
          [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
        ]
    
        // solution 함수 완성
        function solution(K, N, M, chargers) {
          let dp = Array(N+1).fill(0)
          let bat = Array(N+1).fill(0)
          for (const item of chargers){
            bat[item] = 1
          } 

          for (let i=K+1;i<N+1;i++){
            var count = 0
            for (let j = i-K; j<i;j++){
              if (bat[j] === 1){
                dp[i] = dp[j] + bat[j]
                break
              }
              count++
            }
            if (count===K){break}
          }
        console.log(dp[N])

        }
    
        for (const input of inputs) {
          solution(...input)
        }