function evalNumbers(number1, number2, operation) {
    let result;
    
    switch (operation) {
      case "+":
        result = number1 + number2;
        break;
      case "-":
        result = number1 - number2;
        break;
      case "*":
        result = number1 * number2;
        break;
      case "/":
        result = number1 / number2;
        break;
      default:
        console.log(`Invalid operation: ${operation}`);
        return;
    }
    
    console.log(`The result of ${number1} ${operation} ${number2} is ${result}`);
  }
  

  evalNumbers(5, 3, "+"); // The result of 5 + 3 is 8
  evalNumbers(10, 2, "*"); // The result of 10 * 2 is 20
  evalNumbers(8, 4, "/"); // The result of 8 / 4 is 2
  evalNumbers(7, 2, "%"); // Invalid operation: %
  