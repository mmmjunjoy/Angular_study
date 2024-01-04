// getDate - date, day , month

// 인덱스로 구별 - MONTH , DAY


const birthday = new Date("August 19, 1975 23:15:30");
const date1 = birthday.getDate();

console.log(date1);

//------------------------------------------------------

// 여기서 '30' 은 '초'
const birthdayS = new Date('August 19, 1975 23:15:30');
const day1 = birthdayS.getDay();
// Sunday - Saturday : 0 - 6

console.log(day1);
// Expected output: 2

//------------------------------------------------------

// 여기서 '20'은 '분'

const birthdayD = new Date('March 13, 08 04:20');

console.log(birthdayD.getMinutes());
// Expected output: 20

//------------------------------------------------------
// MONTH는 인덱스로 표현 

const ONE = new Date();
const MONTH = ONE.getMonth();


console.log(MONTH);
