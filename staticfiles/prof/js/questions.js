let searchQuestion = document.getElementById('searchQuestion');

searchQuestion.addEventListener('input', () => {
    let inputText = searchQuestion.value.toLowerCase();
    let question = document.getElementsByClassName('list-group-item');
    Array.from(question).forEach(element => {
        let ques_title = element.getElementsByTagName('h3')[0];
        let title = ques_title.innerText.toLowerCase();
        if (title.includes(inputText)) {
            element.style.display = "block";
        }
        else {
            element.style.display = "none";
        }
    })
})
