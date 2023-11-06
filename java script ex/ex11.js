//1:
const helloWorld = () => "Hello World";
//2:
const sayHelloTo = (name) => `Hello ${name} `;
//3:
const squareNumber = (number) => number ** 2;
//4:
const calculateRectangleArea = (length, width) => length * width;
//5:
const calculateCircleMeasurements = (radius) => [2 * Math.PI * radius, Math.PI * radius ** 2];
//6:
const countVowels = (str) => (str.match(/[AEIOUaeiou]/g) || []).length;
//7:
const areArraysEqualLength = (arr1, arr2) => arr1.length === arr2.length;
//8:
const numberToDigitsArray = (number) => Array.from(String(number), Number);
//9:
const mapArrayToFalsyTruthy = (arr) => arr.map((item) => Boolean(item));





