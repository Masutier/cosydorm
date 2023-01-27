
setInterval(createBubble,50)

function createBubble() {
    let bubbleWrapper=document.querySelector('.bubbleWrapper');
    let bubbles = document.createElement('span');
    bubbleWrapper.appendChild(bubbles);

    let randomSizes = 20 + (Math.random() * 50);

    bubbles.style.width = randomSizes + "px";
    bubbles.style.height = randomSizes + "px";
    bubbles.style.left = Math.random() * innerWidth +  "px";

    setTimeout(() => {
        bubbles.remove()
    }, 5500);

}