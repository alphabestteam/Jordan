
const characterMap = new Map();
characterMap.set('Main character', 'spongebob');
characterMap.set('Best friend', 'patrick');
characterMap.set('pet', 'gary');
characterMap.set('word buddy', 'squidward');
characterMap.set('manager', 'Mr. Krabs');
characterMap.set('teacher', 'Mrs. Puff');
characterMap.set('location', 'bikini bottom');


console.log(characterMap);
console.log([...characterMap.keys()]);
console.log(characterMap.get('location'));
console.log(characterMap.size);
characterMap.delete('location');
console.log(characterMap.size);
console.log(characterMap);
console.log(characterMap.has('location'));
