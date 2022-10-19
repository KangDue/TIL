//java script 시작하기

const a = 1 // 값을 선언할 때 값으 넣어 줘야함. let은 선언만 해도 됨.
const b = null // const는 이름 그대로 상수,값을 변경 못함


console.log(a,b) // 여러개의 인자를 ,로 구분 또는 ...
console.log(typeof a) // type 연산자
console.log(a||b) // or
console.log(a&&b) // and 
console.log(a===b) // equal


// let을 이용하면 값 변경 가능한 변수 선언
let c // 변수를 선언했지 정의한 상태가 아님
let d = 1 // 선언과 동시에 값 정의 가능 
let e = 1, f = e*2 // 이렇게 한 번에 여러개 정의도 가능
console.log(c,d,e,f) // c를 보면 정의안해서 undefined가 뜸.
// let, const 여러번 같은 선언 불가, let은 값 변경 가능.
// 변수 이름 지을 때 식별자 첫글자 대문자로 해주는것 camel case(java)
// _로 구분 하는것 snake case (python)
// camel case = fastCampus, snake case = fast_campus

// numer type 은 python 마냥
// 0b, 0o, 0x , _ 사용 가능 .실수 정수 마찬가지
// 정수랑 실수를 별도로 나누지 않음.
// .isInteger 로 판별 가능.
// 기본 산술연산은 파이썬과 같음.
// == 이 ===, != 이 !== 이 된다.
//NaN -0 Infinity -Infinity 도 number 
//NaN 은 유일하게 자기 자신 과 다른 값
//판별하려면 .isNaN 또는 Object.is 함수 써야함.
// 0과 -0도 대부분 같지만, Object.is(0,-0) 하면 다르다고 나옴
// 0으로 나누면 inf, -0은 -inf
// 1/inf = 0, 1/-inf = -0
// inf 판별은 .isFinite method, isFinite 함수도 있지만, method를 권장
// 문자열을 숫자로 바꿀때 parseInt (값, n진수 가능), parseFloat 사용,
// 값이 적절하지 않으면 NaN 값
// 다른 타입이랑 연산 가능하긴 한데 일관적이지 않아서 비추
// 따로 안불러와도 기본 객체(모듈)로 Math가 있다.
// -- 삼각함수, log, exp, sqrt, abs, ceil, floor, round, trunc, max,min, random 등 다양
// number은 .toString, .toLocaleString,, toFixed(소수점아래 n자리) 가 있다.
https://helloworldjavascript.net/pages/140-string.html


if (1){
    console.log("1입니다.")
}
else if (2){
    console.log(3)
}
else{
    console.log("1이 아닙니다.")
}

let i=j=0
while (i<10){
    console.log(++i,j++)
}
// ++i 는 값을 즉시 증가 시키지만
// i++는 현재 값을 반환하고 값을 증가시킨다.
console.log("-------")

let arr=[1,2,3,4,5]
console.log(...arr)
console.log(arr)
console.log(arr[0]) //indexing 가능 하지만 음의 인덱스는 못씀
                    //slicing 불가능

//고전적인 c느낌의 반복문
for (let i=0;i<5;i++){
    console.log(arr[i])
}

//python 같은 반목문
//item 앞에 const를 보통 붙여준다. let도 가능, 안붙여도 무방
for (let item of arr){ 
    console.log(item)
}

// 이상한 형태
// arr의 method 형태로 value와 index를 뽑아올 수 있음
// 대신 값은 value, index, arr 순으로 준다.
arr.forEach( (value,index,arr) => {
    console.log(index,value)
} )

//obj 활용
Object.keys({name:'curryyou', job:'engineer'}); //key
Object.values({name:'curryyou', job:'engineer'}); //value
Object.entries({name:'curryyou', job:'engineer'}); //객체 ['name',curryyou'] 형태

//----------------------
console.log('-----------------')
// 함수 선언
function add1(x,y){
    return x+y
}
// 화살 함수
const add2 = (x,y) => x+y
let add3 = (x,y) => x+y
add4 = (x,y) => x+y
//()로 감싸서 즉석 함수도 가능하다.
console.log(add1(2,3), add2(2,3),add3(2,3),add4(2,3),((x,y)=>x+y)(2,3))

//객체 내부의 attribute와 method 정의간 ,로 구분 해야함.
//python의 dict와 비슷한 형태고 , class가 될 수 도 있음.
const obj = {
    x: 0, // 객체의 속성. 속성 이름: x, 속성 값: 0
    y: 1, // 객체의 속성. 속성 이름: y, 속성 값: 1
    multi: () => this.x*this.y //python의 self = this
  }
  
  // 객체의 속성에 접근하기
  obj.x;
  obj['y'];
  
  // 객체의 속성 변경하기
  obj.x += 1;
  obj['y'] -=1;
  
  // 객체의 속성 삭제하기
  delete obj.x;
console.log(obj.x,obj['x']) // python 처럼 접근은 가능한데 
console.log(obj.y,obj['y']) // [] 접근시 이름은 str 이어야함.
console.log(obj.multi())
