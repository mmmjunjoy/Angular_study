


// let


// let 은 중복선언이 안된다.

// 블럭 내부의 변수는 외부에서 사용할 수 x

// 업데이트는 가능하나, 재선언은 불가하다.


// 업데이트 관련

let update = 1234;

update = 487989;

// 재수정 관련

// let update = 1234;  //오류








// var

// 중복 선언이 가능하다
// 전역 범위 & 함수 범위
// 업데이트나 재선언 둘다 가능하다.
// 이로 인해, const와 let이 탄생 한 것이다.



// function함수

// var 응용

var good = 123;

function goodss() {
  var good = 12345;
  console.log("good", good)
}

this.goodss();


function twotwo() {
  good = 12345567;
  console.log("good2",good)
}

this.twotwo()







// var 의 호이스팅은

// 초기화된다. -> 즉 , undefined상태

// const,let의 호이스팅은

// 초기화 되지 않는다.  -> Reference Error 발생  (참조오류)


var foo = 123;

console.log(foo);


let hi = 456;


console.log(hi);

{

  // number 타입 선언
  let hi3: number = 789;
  let bar = 11;
  console.log(hi);
  console.log(bar);
}

console.log(hi)




// const


// 블록 범위 내에서 가능하다.
// 업데이트도 , 재선언도 불가하다.


// 상수화 시킬떄 사용한다.
// 상수화 시키기 위해선, 반드시 초기값 설정하기



const TOO3 = 123; 
{
  //block level scope
  const TOO = 100;
  console.log(TOO); // 100
  const TOO2 = 45;
}

console.log(TOO3);


// 블럭안에 있는 const 변수는 밖에서 사용 x
// console.log(TOO2);




// const 2

// 객체에도 사용 가능

// key 와  value로 값을 저장하는것이 가능

// const 는 개체는 업데이트 할 수 없으나 , 개체의 '속성'은 업데이트가
// 가능하다.



const obj3 = { id: 7890 };
const obj4 = { bar: 456 };

//다른 객체도 만들어 봅시다
const user_ = {
  name: "devtaco",
  address: {
    city: "Seoul",
  },
};

// 객체명.멤버변수(키명(속성명)) > 값을 불러올때
// 객체명.키명 = 저장할 값  > 저장

console.log(user_); // 여기서는 devtaco
user_.name = "PARK";
console.log(user_.name);