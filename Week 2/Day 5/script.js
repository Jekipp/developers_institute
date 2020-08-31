function hotel_cost(){
  let nights = parseInt(prompt("How many nights?"));
  let hotel_price = 140;
  return nights * hotel_price
}


function plane_ride_cost(){
    let city = prompt("What is your destination?")
      if (city == "London"){
      return 183
      // console.log("$183");
    } else if (city == "Paris"){
      return 220
      // console.log("$220");
    } else if (city != "London" || "Paris"){
      return 300
      // console.log("all other destinations $300");
    }

}



function rental_car_cost(){
  let day = parseInt(prompt("How many days?"))
    if(day <= 10){
      console.log(day * 40);
      return day * 40
    } else {
      console.log( day * (40 * .95));
      return  day * (40 * .95)
    }
}

function total_vaction_cost() {
  let hotel = hotel_cost();
  let plane = plane_ride_cost();
  let car = rental_car_cost()

  return hotel + plane + car

}

console.log(total_vaction_cost());




//
//
//
//
// function hotel_cost(){
//   let nights = parseInt(prompt("How many nights?"));
//   let hotel_price = 140;
//   return nights * hotel_price
// }
// // hotel_cost()
//
// function plane_ride_cost(){
//     let city = prompt("What is your destination?")
//       if (city == "London"){
//       // return $183
//       return 183;
//     } else if (city == "Paris"){
//       // return $220
//       return 220;
//     } else if (city != "London" || "Paris"){
//       return 300
//     }
//
// }
// // plane_ride_cost()
//
//
// function rental_car_cost(){
//   let day = parseInt(prompt("How many days?"))
//     if(day <= 10){
//       // return day * 40
//       return day * 40
//     } else {
//       return day * 40 * .95
//     }
// }
// // rental_car_cost()
//
// function total_vaction_cost(){
//   console.log(hotel_cost() + plane_ride_cost() + rental_car_cost())
// }
//
// total_vaction_cost()
