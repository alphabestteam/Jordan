//1.The difference between accessing an array element using square brackets [index] and using the indexAt(arr) function is that the first way is the standard way to access array elements in JavaScript, while the other function appears to be a custom function 

//ex2:
function createArray(character, number) {
    return Array(number).fill(character);
  }
  
  const newArray = createArray('J', 4);

  //ex3:
  function removeLastNElements(arr, n) {
    if (n >= arr.length) {
      return [];
    }
    return arr.slice(0, arr.length - n);
  }

  //ex4:
  function insertAtBeginning(arr, number) {
    arr.unshift(number);
    return arr;
  }
    //ex5:
  function concatenateArrays(arr1, arr2) {
    return arr1.concat(arr2);
  }
  //ex6:
  function convertToUppercase(strings) {
    return strings.map((str) => str.toUpperCase());
  }
  //ex7:
  function filterTwoDigitNumbers(numbers) {
    return numbers.filter((num) => num >= 10 && num <= 99);
  }
  //ex8:
  function containsValue(arr, value) {
    return arr.includes(value);
  }
  //ex9:
  function findFirstGreaterThanTen(arr) {
    return arr.find((element) => element > 10);
  }
  //ex10:
  function hasNumberGreaterThanTen(arr) {
    return arr.some((element) => element > 10);
  }
  
//11. When you sort an array of numbers using the sort method without specifying a compare function, it treats the numbers as strings and sorts them accordingly.   
  
//ex12:
function sortNumericArray(arr) {
    return arr.slice().sort((a, b) => a - b);
  }

  //ex13:
  function joinWithAsterisks(arr) {
    return arr.join('**');
  }

  //ex14:
  function sortAlphabetically(arr) {
    return arr.slice().sort();
  }
//ex15:
function allNumbersLessThanParameter(arr,parameter) {
    return arr.every((number) => number <parameter);
  }

  //ex16:
  function hasElementGreaterThanParameter(arr,parameter) {
    return arr.some((element) => element >parameter);
  }
  
  
  



  
  
  

  