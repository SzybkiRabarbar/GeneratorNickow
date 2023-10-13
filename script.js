// Function to fetch a random word from a text file
function getRandomWord(file) {
    return fetch(file)
        .then(response => response.text())
        .then(data => {
            const lines = data.split('\n');
            const randomIndex = Math.floor(Math.random() * lines.length);
            return lines[randomIndex];
        });
}

// Function to capitalize a word
function capitalize(word) {
    return word.charAt(0).toUpperCase() + word.slice(1);
}

// Randomly choose whether to use male or female words
const gender = Math.random() < 0.5 ? 'm' : 'w';

// Fetch the random adjective and noun
Promise.all([
    getRandomWord(`WordsLists/przymiotniki-${gender}.txt`),
    getRandomWord(`WordsLists/rzeczowniki-${gender}.txt`)
]).then(words => {
    // Capitalize the words
    const capitalizedWords = words.map(capitalize);

    // Insert the words into the HTML document
    document.getElementById("randomWords").innerHTML = capitalizedWords.join(' ');
});
