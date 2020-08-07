var header = document.querySelector("body")

header.style.backgroundColor = 'red'

function getRandomColor() {
    var letters = "0123456789ABCDEF";
    var color = '0000';
    for (var i = 0; i < 2; i++) {
        color = letters[Math.floor(Math.random() * 16)] + color;
    }
    color = '#' + color;
    return color
}


function changeHeaderColor() {
    colorInput = getRandomColor();
    header.style.backgroundColor = colorInput;
}


setInterval("changeHeaderColor()", 500);