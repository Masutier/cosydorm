
setInterval(createBubbleI,50)

function createBubbleI() {
    let bubbleWrapperI=document.querySelector('.bubbleWrapperI');
    let bubblesI = document.createElement('span');
    bubbleWrapperI.appendChild(bubblesI);

    let randomSizes = 20 + (Math.random() * 50);

    bubblesI.style.width = randomSizes + "px";
    bubblesI.style.height = randomSizes + "px";
    bubblesI.style.left = Math.random() * innerWidth +  "px";

    setTimeout(() => {
        bubblesI.remove()
    }, 5500);

}
