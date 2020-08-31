//xp 1
let color = ["red", "blue", "yellow", "purple", "green","orange"]
// // for(i = 0; i < color.length; i++){
// // console.log("my favorite color is ", color)
// // }
//
for(let favColor of color){
  console.log("my favorite color is ", favColor);
}

for (i in colors){
  console.log("my #" + parseInt(i) + 1) +" color is " + color[i]);
}
//
// //xp 2
let names = ["Jack", "Philip", "Sarah", "Amanda", "Kyle"];
names = names.sort();
let society = "";
for (let name of names){
  society = society + name.charAt(0);
}
console.log(society);
//

// let sorted_names = names.sort();
names.sort();
let secret = '';
for(name of names){
  secret += name.charAt(0)
}
  console.log(secret);
//+= plus equals add the next iterate


console.log(typeof(i));

// for(i = 0, i > names.length; i++);
// let secretSociety =
//
//   initial of names = charAt(0)){
//   console.log(initial);
// }


// xp 3
let number = parseInt(prompt("Enter Number: "));
while (number < 10){
  number = parseInt(prompt("Enter a new number: "));
}
console.log("Big Number");


// let group = names.sort()
//   console.log(group)



// xp 4
let people = ["Greg", "Mary", "Devon", "James"]
for (let i of people){
  console.log(i);
people.splice(0,1);
  console.log(people);
// break;
people.splice(2,1,"Jason");
  console.log(people);
people.splice(3,0,"Jackie")
  console.log(people);
people.indexOf("Mary")
  console.log(people.substring(0, indexOf("Mary")))
  break;
}


for (person of people){
  console.log(person);
}
people.shift();
  console.log(people);

//people[3] = "Jason"
//people.splice(2, 1, "Jason")
people.splice(people.indexOf("James"), 1, "Jason")
console.log(people);

people.push = ("Jonathan")

for (person of people){
  if (person == "Mary"){4
  console.log(person);
  break;
  }
}

let people_copy = people.slice(0, people.indexOf("Mary")) + people.indexOf("Mary") + 1, people.indexOf("Jonathan")) + people.indexOf(people.slice)

console.log(people[people.length -1]);


//

let arr = ["a", "b", "c"]
let last_item = arr.pop()

// let names = ["Jack", "Philip", "Sarah", "Amanda", "Kyle"];
// names = names.sort();
// let society = "";
// for (let name of names){
//   society = society + name.charAt(0);
// }
// console.log(society);



// // exercise 2
// for ( let i = 0; i <= 15; i++){
//   if(i%2 == 0){
//   console.log("even " + i)
// } else {
//   console.log("odd " + i)
// }
// }
//
// let numbers = ["a", "b", "c", "d"]
//
// for (let index in numbers)
// console.log(index)
//
//
// let family = {
//   members: ["mom", "dad"],
//   numberMembers: 2,
//   familyName: "Smith",
//   hasPet: true
// }
//
// for(let key in family){
//   console.log(key)
// }
//
// for (let property in family){
//   if (property === "familyName"){
//     if(family[property] === "Smith"){
//       console.log("Hello Smith family")
//     } else{
//       console.log("I dont know you");
//     } else {
//       console.log("No familyName");
//     }
//   }
//
// for (let property in family){
//   console.log("property:", property)
//   console.log("value :" family[property])
// }
//
//
// // 1. Loop through the array of object
// // 2. If the username is Sarah : say hello to her friends (display the name of her friends)
// // 3. If the username is Dan : change his password to 567​
// // --> can use switch
// // --> for in or for of
// ​
// ​
// let users = [
//     {
//         username: "Sarah",
//         password: 123,
//         friends: ["max", "tom"]
//     },
//     {
//         username: "Dan",
//         password: 433
//     }
// ]
//
//
// for(let person of users)
//   if(person.username === "Sarah"){
//     for(let partner of person.friends){
//     console.log("My friend is", partner);
//   }
// } else if person.username === "Dan"){
//   for(let newcode of person.username.password){
//
//   }
// }
//
//
// //exercise 3
//
// let names = [
//     {
//         username: "John",
//         password: 123,
//     },
//     {
//         username: "Sara",
//         password: 433
//     }
// ]
//
//
// let counter = 1
// while (counter < 10){
//   console.log("counter is ", counter)
//   counter++
// }
//
//
// let counter = 1
// do{
//   console.log("counter is ", counter)
//   counter++
// }
// while (counter < 10){
// }
//
// let counter = 1
// do{
//   alert("Hello user")
// }
// while (counter < 10){
//   counter++
// }
