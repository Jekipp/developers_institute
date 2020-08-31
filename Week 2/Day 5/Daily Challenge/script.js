
let num1 = [];
let operator = "";
let first_num;
let second_num;

function my_f(button) {
  if (typeof(button) == 'string' && button != "=") {
    operator = button;
    first_num = parseInt(num1.join(""));
    num1 = [];
  } else if (button == "=") {
    second_num = parseInt(num1.join(""));
    switch(operator) {
      case "+":
        return first_num + second_num;
      case "-":
        return first_num - second_num;
      default:
        return first_num / second_num;
    }
  } else {
    num1.push(button);
  }

}
