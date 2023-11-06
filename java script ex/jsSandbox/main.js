const myHeading = document.getElementById('main-heading');

console.log('ID:', myHeading.id);
console.log('Class Name:', myHeading.className);
console.log('Class List:', myHeading.classList);
console.log('Data Attribute (dataset):', myHeading.dataset.standardNonAttribute);
console.log('Data Attribute (getAttribute):', myHeading.getAttribute('data-standard'));
myHeading.classList.add('bg-lightcyan', 'border');
console.log('Text Content:', myHeading.textContent);
console.log('Text Content Without Whitespaces:', myHeading.textContent.trim());

myHeading.textContent = 'Hello there pearl!';
myHeading.innerHTML += '<br><span>its me SpongeBob!</span>';
console.log(myHeading);
const cloned = myHeading.cloneNode(true);
console.log('Cloned Element:', cloned);
const subheading = document.createElement('h2');
subheading.textContent = 'jellyfish hunting is the best!';
document.body.appendChild(subheading);

const loremIpsumText = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Labore eum, earum deserunt numquam quis explicabo. Delectus id, cum voluptate dicta aperiam sunt voluptatum quis eaque aliquam distinctio reiciendis iste minima?";
const loremIpsumWordArr = loremIpsumText.split(/\s+/);

const colors = ['red', 'orange', 'yellow', 'greenyellow', 'lightblue', 'mediumpurple'];
function getRandomColor() {
    const randomIndex = Math.floor(Math.random() * colors.length);
    return colors[randomIndex];
}

const wordsRandomElement = document.getElementById('random-words');


loremIpsumWordArr.forEach(word => {
    const spanElement = document.createElement('span');
    const style = "background-color: "+ getRandomColor();
    spanElement.setAttribute("style", style)
    spanElement.textContent = word;
    spanElement.className = "random-words";
    wordsRandomElement.appendChild(spanElement)
});

changeColorButton.addEventListener("click", changeTextColor);

function changeTextColor() {
    const randomWordElements = document.querySelectorAll('.random-words');
    randomWordElements.forEach(wordElement => {
        const randomColor = getRandomColor();
        wordElement.style.backgroundColor = randomColor;
    });
}



