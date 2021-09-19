window.smoothScroll = function(target) {
    var scrollContainer = target;
    do { 
        scrollContainer = scrollContainer.parentNode;
        if (!scrollContainer) 
            return;

        scrollContainer.scrollTop++;
    } while (scrollContainer.scrollTop == 0);

    var targetY = 0;
    do { 
        if (target == scrollContainer)
            break;

        targetY += target.offsetTop;
    } while (target = target.offsetParent);

    scroll = (c, a, b, i) => {
        i++; 
        if (i > 30) 
            return;
        c.scrollTop = a + (b - a) / 30 * i;
        setTimeout(() => { scroll(c, a, b, i); }, 20);
    }
    
    scroll(scrollContainer, scrollContainer.scrollTop, targetY, 0);
}

let searchExam = document.getElementById('searchExam');

searchExam.addEventListener('input', () => {
    let inputText = searchExam.value.toLowerCase();
    let examCard = document.getElementsByClassName('card');
    Array.from(examCard).forEach(element => {
        let exam_title = element.getElementsByTagName('h3')[0];
        let title = exam_title.innerText.toLowerCase();
        if (title.includes(inputText)) {
            element.style.display = "block";
        }
        else {
            element.style.display = "none";
        }
    })
})

$( () => {
    $('.datetime-input').datetimepicker({
        format:'DD-MM-YYYY HH:mm'
    });
});