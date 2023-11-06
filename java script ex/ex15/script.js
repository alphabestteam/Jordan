const showBobButton = document.getElementById('the-button');
const bobGif = document.getElementById('bob');

bobGif.style.display = 'none';
showBobButton.textContent = 'Show me Bob:)';

showBobButton.addEventListener('click', function() {
    if (bobGif.style.display === 'none') {
        bobGif.style.display = 'block';
        showBobButton.textContent = 'Hide Bob:)';
    } else {
        bobGif.style.display = 'none';
        showBobButton.textContent = 'Show me Bob:)';
    }
});
