// let age = parseInt(prompt(“What is your age?”));

// if (Number(age) < 18) {
//     alert("Sorry, you are too yound to drive this car. Powering off");
// } else if (Number(age) > 18) {
//     alert("Powering On. Enjoy the ride!");
// } else if (Number(age) === 18) {
//     alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
//
// function check_driver_age(){
//   if (Number(age) < 18) {
//       alert("Sorry, you are too yound to drive this car. Powering off");
//   } else if (Number(age) > 18) {
//       alert("Powering On. Enjoy the ride!");
//   } else if (Number(age) === 18) {
//       alert("Congratulations on your first year of driving. Enjoy the ride!");
//   }
// }


function check_driver_age(){
  let age = parseInt(prompt("How old are you?"));
  if (age < 18) {
      alert("Sorry, you are too yound to drive this car. Powering off");
    } else if (age > 18) {
        alert("Powering On. Enjoy the ride!");
    } else if (age === 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    }
}

check_driver_age();
//2
//Create a function called checkBasket().
// It should:
// // ask the user for the item he wants
// // and let him know if it’s in the basket or not
amazonBasket = {
    'glasses': 1,
    'books': 2,
    'floss': 100
}

function check_basket(){
  let wanted_object = prompt("What do you want?");
  if(amazonBasket[wanted_object]) {
    console.log("Exists");
  } else {
    console.log("DNE");
  }
}
check_basket();



let money = [25, 10, 5, 1]

function changeEnough(wallet_array, total_due) {
  let my_money = (.25 * wallet_array[0]) + (.1 * wallet_array[1]) + (.05 * wallet_array[2]) + (.01 * wallet_array[3]);
  if (my_money >= total_due) {
    console.log("afford");
  } else {
    console.log("Can't afford");
  }
}
changeEnough(money, 12.30);


//4

let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}


let list = [
  {"name": "apples", "quantity": 5},
  {"name": "oranges", "quantity": 13},
  {"name": "banana", "quantity": 8},
]
// let list = ["apple", "orange",  "banana"];
let total = 0
function in_stock(name){
  return stock[item] > 0
}

function buy(item){
  total += prices[item] > 0
  stock[item] -= 1;
  // stock[item] = stock[item] - 1,
}

function buy(item){
  if (item["quantity"]) > stock[item["name"]]){
    item["quantity"] = stocl[item["name"]];
  }
total += (prices[item["name"]] * item["quantity"]);
stock[item["name"]] -= item["quantity"];
}

for (item of list){
  // if(in_stock[item])
  if(in_stock(item["name"])){

  }
}

buy()



//5

function hotel_cost(nights){
  let nights = parseInt(prompt("How long is your stay?"));
  return (nights * 140);
}
hotel_cost()

function plane_ride_cost(city){
    let city = prompt("What is your destination?"){
      if (city == "undefined"){
        city = prompt("Enter your destination again")
    } else if (city == "London"){
      return $183
    } else if (city == "Paris"){
      return $220
    } else if (city != "London" || "Paris"){
      return all other destinations $300
    }
  }
}

function rental_car_cost(day){
  let day = parseInt(prompt("How many days?")){
    if(day <= 10){
      return day * 40
    } else {
      return day * (40 * .95)
    }
}

function total_vaction_cost(nights, city, day){
  return hotel_cost + plane_ride_cost + rental_car_cost
}

total_vaction_cost()
