// //daily challenge
// let str1 = "This dinner is not bad!";
// let findNot = str1.indexOf("not");
// let findBad = str1.indexOf("bad");
// if (findNot < findBad && findNot != -1){
//   console.log(str1.substr(0, findNot) + "good!");
// }
// else {
//   console.log(str1);
// }
//
// let str2 = "This dinner is bad!";
// let findNot2 = str2.indexOf("not");
// let findBad2 = str2.indexOf("bad");
// if (findNot2 < findBad2 && findNot2 != -1){
//   console.log(str2.substr(0, findNot2) + "good");
// }
// else {
//   console.log(str2);
// }
// let str2 = str1.split(" ");
// console.log(findNot);
// console.log(str2.length);
// let findNot = str2.indexOf("not");
// console.log("not is located at " + findNot);
// let findBad = str2.indexOf("bad");
// console.log("bad is located at " + findBad);

// exercise xp gold
// 1
// let userWord = prompt("Your Word Here:");
// let noVowel = userWord.replace(/[aeiou]/g, " ");
// alert(noVowel);

// 2
// let language = prompt("Do you speak French, English or Hebrew?");
// switch (language){
//   case "french":
//     alert("bonjour");
//     break;
//   case "english":
//     alert("Hello");
//     break;
//   case "hebrew":
//     alert("Shalom");
//     break;
//   default:
//     alert("illiterate");
// }


//3
// let grade = parseInt(prompt("What is your grade?"));
//   if (grade >= 90){
//     alert("A");
//   } else if (grade < 90 && grade >= 80){
//     alert("B");
//   } else if (grade < 80 && grade >= 70){
//     alert("C");
//   } else if (grade < 70 && grade >= 60){
//     alert("D");
//   } else if (grade < 60){
//     alert("F");
//   }

  //4

let userZip = prompt("What is your Zip Code?");
  if (userZip.length == 5 && isNaN(userZip) == false) {
    alert("You've got mail")
} else {
  alert("Fail")
  }
