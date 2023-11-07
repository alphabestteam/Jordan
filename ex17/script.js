const main = document.querySelector('main');
function createHeading(color, text){
    const heading = document.createElement('h1');
    heading.setAttribute('style', 'color: ' + color);
    heading.textContent = text;
    return heading;
}

function headingFactory(color) {
    return function (text) {
        const heading = createHeading(color, text);
        return heading;
    };
}


const createRedHeading = headingFactory('red');
const createBlueHeading = headingFactory('blue');

main.appendChild(createRedHeading(' using Factory 1'));
main.appendChild(createBlueHeading('using Factory 2'));
