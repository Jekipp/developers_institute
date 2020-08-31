// let addressNumber = "770 "
// let addressStreet = "Hayarkon "
// let country = "Israel"
// let global_address = "I live at " + addressNumber + addressStreet + country
//
//
// let str = "Hello\n";
// console.log(str.repeat(5));
//
// let money = 123.888
// let roundMoney = money.toFixed(2)
// console.log(roundMoney)
//
// let birthYear = 1987
// let futureYear = 2020
// console.log("I will be " + (futureYear - birthYear) + " in " + futureYear);
//
//
// let pets = ['cat','dog','fish','rabbit','cow']
// console.log(pets[1])
// pets.push("horse")
// pets.splice(3,1)

var array = ["banana", "apples", "oranges", "blueberries"];
console.log(array.splice(0,1));
array.push("kiwi");
array.splice(0,1);
console.log(array.reverse());

console.log(5 + "34");
console.log(5 - "4");
console.log(10 % 5);
console.log(5 % 10);
console.log("Java" + "Script");
console.log(" " + " ");
console.log(" " + 0);
console.log(true + true);
console.log(true + false);
console.log(false + true);
console.log(false - true);
console.log(3 - 4);
console.log("Bob" - "bill");

console.log(5 >= 1);
console.log(0 === 1);
console.log(4 <= 1);
console.log(1 != 1);
console.log("A" > "B");
console.log("B" < "C");
console.log("a" > "A");
console.log("b" < "A");
console.log(true === false);
console.log(true != false);

console.log("Hi there It's sunny" + " outside")

let a = 34;
let b = 21;
a = 2;
console.log(a+b);
let c;
console.log(c)
c = 10
console.log(a + b + c)

let findNemo = "I found Nemo";
let foundnemo = findNemo.split(" ");
console.log(foundnemo);
console.log(findNemo.length);
let nemo = foundnemo.indexOf("Nemo");
console.log("I found Nemo at " + nemo)


let firstNumber = parseInt(prompt("Enter 1st Number"));
let secondNumber = parseInt(prompt ("Enter 2nd Number"));
console.log(firstNumber + secondNumber);
alert(firstNumber + secondNumber)
