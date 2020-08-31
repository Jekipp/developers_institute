// //1. Create a function called shopping, that takes 1 parameter --> Array
// 2. Inside the function, you have to go through the array and console.log each fruit that you bought
// 3. Call the function
//
// 4. Add 2 new parameters --> currency and amount of money
// 5. Mutiply the amount of money by 3.50
// 6. Console log the amount you paid and the currency

let fruit = [
  {
  "name": "apple",
  "currency": ["nis", "$"],
  "price": 3,
};
{
"name": "banana",
"currency": ["nis", "$"],
"price": 5,
};
{
"name": "cherry",
"currency": ["nis", "$"],
"price": 1,
};
]

//

function shopping (fruit, currency, price){
  if("cherry"){
  console.log((fruit[0].price) * 3.5 + fruit[0].currency[0]);
  }  if else
  console.log(fruit);
}


shopping(["apple", "banana", "cherry"], "$", 150)
function shopping (shoppinglist, currency, money){
  for (fruit of shoppinglist){
    console.log(fruit);
  }
  money * 3.5
  console.log("I spent " + money + currency)
}

//
let h1 = document.getElementById("title")

function changeBackground(){
  h1.classList.add("ocean")
}

//

function addParagraph(sentence){
  let p = document.createELement("p")
    p.style.fontSize = "25px"
    p.style.color = "purple"
  let text = document.createTextNode(sentence)
    p.appendChild(text)
  let divs = document.getElementsByTagName("div")
    for (element of divs){
      element.appendChild(p)
    }
}


addParagraph("Hello Students")



//

let div = document.getElementsByTagName("div")[0]
//gets first div on page

document.querySelectorAll("div h3")
//querySelector works in css
//returns nodeList



//remove all outgoing friend requests

var inputs = document.getElementsByClassName('_54k8 _52jg _56bs _26vk _2b4n _56bt');
for(var i=0; i != inputs.length; i++) {
inputs[i].click();
}

var inputs = document.getElementsByClassName('_54k8 _56bs _56bt');
 for(var i=0; i<inputs.length;i++) {
 inputs[i].click();
}

//invite all friends to group
var inputs = document.getElementsByClassName(‘uiButton _1sm’);
for(var i=0; i<inputs.length;i++) {
   inputs[i].click();
 }
