
setInterval(createBubbleIII,50)

function createBubbleIII() {
    let bubbleWrapperIII=document.querySelector('.bubbleWrapperIII');
    let bubbles = document.createElement('span');
    bubbleWrapperIII.appendChild(bubbles);

    let randomSizes = 20 + (Math.random() * 50);

    bubbles.style.width = randomSizes + "px";
    bubbles.style.height = randomSizes + "px";
    bubbles.style.left = Math.random() * innerWidth +  "px";

    setTimeout(() => {
        bubbles.remove()
    }, 5500);

}