
setInterval(createBubbleII,50)

function createBubbleII() {
    let bubbleWrapperII=document.querySelector('.bubbleWrapperII');
    let bubbles = document.createElement('span');
    bubbleWrapperII.appendChild(bubbles);

    let randomSizes = 20 + (Math.random() * 50);

    bubbles.style.width = randomSizes + "px";
    bubbles.style.height = randomSizes + "px";
    bubbles.style.left = Math.random() * innerWidth +  "px";

    setTimeout(() => {
        bubbles.remove()
    }, 5500);

}