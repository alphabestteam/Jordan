// 1. creating a const array with 5 friends names
const friends = ["SpongeBob", "Patrick", "Squidward", "Sandy", "Mr. Krabs"];

// 2. Print the array and the length
console.log("Initial array:", friends);
console.log("Array length:", friends.length);

// 3. Add a new friend
friends.push("Plankton");

// 4. Print the array after adding a friend and its updated length
console.log("Updated array:", friends);
console.log("Updated array length:", friends.length);

// 5. Change the first item in the array to a different friend
friends[0] = "Gary";

// 6. Print the updated array
console.log("Array after changing the first item:", friends);

/*
 7. I can change the values of the array elements even though the array is declared as const
because The reference to the array itself is constant, but the content and values inside the array can still change.
*/
