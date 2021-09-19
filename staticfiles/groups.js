let searchGroup = document.getElementById('searchGroup');

searchGroup.addEventListener('input', () => {
    let inputText = searchGroup.value.toLowerCase();
    let groupCard = document.getElementsByClassName('card');
    Array.from(groupCard).forEach(element => {
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
