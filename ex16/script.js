function addEvent() {
    const button = document.getElementById('my-button');
    const counterDisplay = document.getElementById('counter-display');
    
    let count = 0;

    button.addEventListener('click', function() {
        count++;
        counterDisplay.textContent = count;
    });

}
addEvent();