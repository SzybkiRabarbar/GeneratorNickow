fetch('WordsLists/przymiotniki-m.txt')
    .then(response => response.text())
    .then(data => {
        const lines = data.split('\n');
        const randomIndex = Math.floor(Math.random() * lines.length);
        const randomWord = lines[randomIndex];
        document.getElementById("randomWord").innerHTML = randomWord;
    });