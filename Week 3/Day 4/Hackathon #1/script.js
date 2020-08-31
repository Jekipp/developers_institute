// let buttons = document.getElementByTagname("button");
//
// // for (let button of buttons){
//
// for (let i = 0; i < 100; i++){
//   let button = createButton();
//
//
//   button.addEventListener("click", function(event){
//     changeColor(event.target);
//   });
// }
//
//
// function changeColor(target) {
//   if (target.style.backgroundColor == "blue"){
//     target.style.backgroundColor = "red";
//   } else{
//     target.style.backgroundColor = "blue"
//   }
// }
//
// function createButton() {
//   let button = document.createElement("button");
//
// }


let number = [1,2,3,4,5,6,7,8,9,10]

function largestNumber(number){
  let bigNumber = 0;
  for (item of number){
    if (bigNumber < item){
      bigNumber = item;
    }
  }
  console.log(bigNumber);
}

largestNumber(number)


function total(number) {
  let total = 0;
  for (num of number){
    total += num;
  }
  for (i = 0; i < number.length; i++){
  }
  return total
}

function average(numbers){
  let total(numbers) / number.length;
}

function analyze_numbers(number){
  return{
    "biggest": largestNumber()
    "total": total()
    "average": average()
  }
}



//
let upper = 9;
let lower = 0;

function make_guess(upper, lower){
  return Math.round((upper - lower) / 2)
}

do{
  user_input = prompt("My guess is " + my_guess + ". What do you think? (h/l/c)")
  if (user_input == "h"){
    lower = my_guess
  }
  else if (user_input == "l"){
    upper = my_guess
  }
}while (user_input != "c")
alert ("I win")
