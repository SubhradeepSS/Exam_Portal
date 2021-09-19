let searchPaper = document.getElementById('searchPaper');

searchPaper.addEventListener('input', () => {
    let inputText = searchPaper.value.toLowerCase();
    let paperCard = document.getElementsByClassName('card');
    Array.from(paperCard).forEach(element => {
        let paperTitle = element.getElementsByTagName('h3')[0];
        let title = paperTitle.innerText.toLowerCase();
        if (title.includes(inputText)) {
            element.style.display = "block";
        }
        else {
            element.style.display = "none";
        }
    })
})
