// js의 객체 생성자는 {}
// 만들때 propery나 attibute의 이름을 str값을 하든 안하든 똑같다.
// 구버전 ECMAScript5 는 오류가 날 수도,나면 ''감싸주면 됨.
var foo = {name:1,'num':2}
console.log(foo)
delete foo.name // delete 로 삭제 가능
// null 또는 undefined 할당은 value만 바꾸는것
console.log(foo)

//null과 undefined이외의 모든게 객체 처럼 동작
// 단 int는 .method를 js parser가 오류로 인식하는데
// 아래처럼 해결 가능
2..toString() // 점 2개
2 .toString() // 공백
// (2).toString() //감싸기 -- 이건 안먹히네 ? 


// Prototype
// js는 class 상속 모델이 아닌 prototype 상속 모델을 사용
// prototype chain을 이용해 상속 구현
function Go() {
    this.value = 42; // 단순 호출시 global을 this로 찾아감.
}

Go.prototype = {
    method : function() {console.log("go 프로토")}
};

function Back() {};

Back.prototype = new Go(); //단순 instance 할당
Back.prototype.Go = "Hellow~" //프로토타입은 obj에서 직접 참조 안됨.

Back.prototype.constructor = Back

var test = new Back()
console.log(Back.prototype.Go)
// 뭔데 상속도 안되고 이상하누;
// 객체의 프로퍼티의 접근하려 하면 js는 prototype chain을 거슬러 올라가
// 해당 property를 찾음 like python
// 없으면 undefined 반환

// ! prototype property 는 프로토타입 체인을 만들 때 사용하고
// 어떤 값이든 할당 가능하다.
// primitive 값을 할당되면 무시한다.
// string, number, bigint, boolean, undefined, symbol, (null)(원시 자료형 int ,str 같은)
// 객체.hasOwnProperty('프로퍼티명') 으로 property를 직속으로 가지고 있는지 bool값 반환
// 위 method 조차 property다.


// 이러면 chain까지 다 살펴봄, in 연산자들이 이런다.
// Object.prototype을 오염시킨다.
Object.prototype.bar = 1;
var foo = {moo: 2};
for(var i in foo) {
    console.log(i); // bar와 moo 둘 다 출력한다.
}

// - 따라서 아래와 같이 수정해서 써야 옳음
for(var i in foo) {
    if (foo.hasOwnProperty(i)) {
        console.log(i);
    }
}

//---------------------------
// 함수는 first class obj다.
// 함수 자체가 다른 함수의 인자가 될 수 있다.
// 그래서 익명 함수를 비동기 함수의 콜백으로 넘김

// 1. function 을 이용해 선언시 hoist scope 형성 됨.
// var라는 변수 선언도 hoist scope를 형성 시킴.

// 1-1 이름 있는 함수 표현 식
var foo = function bar() { //foo가 있는 scope에 아무것도 없음.
                        // bar()도 foo 내부에 존재.
    bar(); // 이 경우는 동작 하지만, 
}
// foo() 무한 재귀
// bar(); // 이 경우는 참조에러를 발생시킨다.
// foo 내부에만 존재하니까 참조에러


//----------------------------
// this의 이해
// 1. 그냥 this = global obj
// 2. 단순 함수 호출 = global obj
// 3. method를 통한 호출 ex)test.go() , method를 가진 객체 // 함정 method 내보의 함수는 global
// 4. new Go() 로 생성자 호출 시 새로 생긴 instance 가리킴
// this가 가리킬 객체 골라주기
// call, apply, bind
const obj = {num : 1}
const get = function(content){
    console.log(content +' '+ this.num.toString())
}
// get('번호는~') 여기서는 this가 global obj를 가리킴.
// 아래 둘가 첫 인자는 this가 가리킬 객체
get.call(obj,'번호는~') // call 의 나머지는 함수에 들어갈 인자 ,로 구분 나열
get.apply(obj,['번호는~']) //apply는 나머지 인자를 arr 형태로 담아서 넘기기
let new_get = get.bind(obj) // 위 2개랑 다르게 this 값을 지정한 새 함수(Bound 함수)를 반환 한다.
new_get('번호는!')





//나중에 공부해보기
// http://bonsaiden.github.io/JavaScript-Garden/ko/
// https://wooooooak.github.io/kotlin/2022/01/11/%EB%9E%8C%EB%8B%A4%EB%82%B4%EB%B6%80%EC%97%90%EC%84%9C%EC%9D%98return/
// Method 할당하기
// JavaScript의 또다른 함정은 바로 함수의 별칭을 만들수 없다는 점이다. 별칭을 만들기 위해 메소드를 고 바로 할당해 버린다.
// 변수에 넣으면 자바스크립트는 별칭을 만들지 않