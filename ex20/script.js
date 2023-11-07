

document.addEventListener("DOMContentLoaded", function () {
    const quoteDisplay = document.getElementById("quote");
    const inputElement = document.getElementById("input");
    const startButton = document.getElementById("start-btn");
    const timerElement = document.getElementById("timer");
    const resultElement = document.getElementById("result");
    const leaderboardTable = document.getElementById("leaderboard");

    // Load previous results from localStorage
    let leaderboard = JSON.parse(localStorage.getItem("leaderboard")) || [];

    let timerInterval;
    let startTime;

    function getRandomQuote() {
        const quotes = [
            "I'm ready, I'm ready, I'm ready! - SpongeBob SquarePants",
            "F is for friends who do stuff together, U is for you and me, N is for anywhere and anytime at all! - SpongeBob SquarePants",
            "I'm not just ready, I'm ready Freddy! - SpongeBob SquarePants",
            "Remember, licking doorknobs is illegal on other planets. - SpongeBob SquarePants",
            "The inner machinations of my mind are an enigma. - Patrick Star",
            "I can't hear you, it's too dark in here! - Patrick Star",
            "I'm ugly and I'm proud! - SpongeBob SquarePants",
            "I'll have you know that I stubbed my toe last week while watering my spice garden and I only cried for 20 minutes. - Squidward Tentacles",
            "Once there was an ugly barnacle. He was so ugly that everyone died. The end. - Patrick Star",
            "Is mayonnaise an instrument? - Patrick Star",
            "Can you give SpongeBob his brain back? - Patrick Star",
            "I guess hibernation is the opposite of beauty sleep. - Squidward Tentacles",
            "I know of a place where you never get harmed. A magical place with magical charms. Indoors! Indoors! Indoors! - SpongeBob SquarePants",
            "I can't believe I'm finally wearing a Krusty Krab hat. Promotion, here I come! - SpongeBob SquarePants",
            "I'll take a double triple bossy deluxe on a raft, 4x4, animal-style, extra shingles with a shimmy and a squeeze, light axle grease, make it cry, burn it, and let it swim. - Bubble Bass",
            "Sandy: What do you usually do when I'm gone? SpongeBob: Wait for you to come back.",
            "SpongeBob: Don't worry, Mr. Krabs, I'll have you out of there faster than a toupee in a hurricane!",
            "SpongeBob: I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors. - Squidward: What's that? - SpongeBob: Outdoors.",
            "SpongeBob: Can I be excused for the rest of my life?",
            "SpongeBob: I'm not just ready, I'm ready Freddy!",
            "SpongeBob: You don't need a license to drive a sandwich.",
            "SpongeBob: Goodbye everyone, I'll remember you all in therapy.",
            "SpongeBob: Patrick, I don't think Wumbo is a real word. Patrick: Come on, SpongeBob, we're best friends. I would never call you a Wumbologist if I didn't think you were one.",
            "SpongeBob: I'm a Goofy Goober, yeah. You're a Goofy Goober, yeah. We're all Goofy Goobers, yeah. Goofy, goofy, goober, goober, yeah!",
            "SpongeBob: Once there was an ugly barnacle. He was so ugly that everyone died. The end."
             ];
                const randomIndex = Math.floor(Math.random() * quotes.length);
                return quotes[randomIndex];
    }

    function startGame() {
        clearInterval(timerInterval);
        quoteDisplay.innerHTML = '';
        const quoteText = getRandomQuote();
        quoteText.split('').forEach(char => {
            const charSpan = document.createElement('span');
            charSpan.innerText = char;
            quoteDisplay.appendChild(charSpan);
        });
        inputElement.value = "";
        inputElement.classList.remove("correct", "incorrect");
        inputElement.disabled = false;
        inputElement.focus();

        startButton.disabled = true;
        timerElement.textContent = "Time: 0 seconds";

        let seconds = 0;
        timerInterval = setInterval(() => {
            seconds++;
            timerElement.textContent = `Time: ${seconds} seconds`;
        }, 1000);

        startTime = Date.now();
    }

    function checkInput() {
        const quoteText = quoteDisplay.children;
        const inputText = inputElement.value;

        for (let i = 0; i < quoteText.length; i++) {
            const inputChar = inputText[i];
            const quoteChar = quoteText[i];

            if (!inputChar) {
                quoteChar.classList.remove("correct", "incorrect");
            } else if (inputChar === quoteChar.innerText) {
                quoteChar.classList.remove("incorrect");
                quoteChar.classList.add("correct");
            } else {
                quoteChar.classList.remove("correct");
                quoteChar.classList.add("incorrect");
            }
        }

        if (inputText.length === quoteText.length) {
            endGame();
        }
    }

    function endGame() {
        clearInterval(timerInterval);
        inputElement.disabled = true;
        startButton.disabled = false;

        const endTime = Date.now();
        const elapsedSeconds = (endTime - startTime) / 1000;
        const wordsTyped = inputElement.value.split(/\s+/).filter(word => word !== "").length;
        const wpm = Math.round((wordsTyped / elapsedSeconds) * 60);
        const accuracy = calculateAccuracy(inputElement.value, Array.from(quoteDisplay.children).map(char => char.innerText).join(''));
        const score = wpm * (accuracy / 100) * 2;

        
        leaderboard.push({ words: wordsTyped, time: elapsedSeconds, wpm, accuracy, score });
        leaderboard.sort((a, b) => b.score - a.score);
        localStorage.setItem("leaderboard", JSON.stringify(leaderboard));
        displayLeaderboard();

        resultElement.textContent = `Words Typed: ${wordsTyped} | Time: ${elapsedSeconds} seconds | Speed (WPM): ${wpm} | Accuracy: ${accuracy}%`;
    }

    function calculateAccuracy(userText, originalText) {
        const matchingChars = countMatchingChars(userText, originalText);
        const totalChars = Math.max(userText.length, originalText.length);
        const accuracy = (matchingChars / totalChars) * 100;
        return Math.round(accuracy);
    }

    function countMatchingChars(strA, strB) {
        let count = 0;
        const minLength = Math.min(strA.length, strB.length);
        for (let i = 0; i < minLength; i++) {
            if (strA[i] === strB[i]) {
                count++;
            }
        }
        return count;
    }

    function displayLeaderboard() {
        leaderboardTable.innerHTML = `
            <tr>
                <th>Rank</th>
                <th>Words</th>
                <th>Time</th>
                <th>WPM</th>
                <th>Accuracy</th>
                <th>Score</th>
            </tr>
        `;
    
        leaderboard.forEach((entry, index) => {
            const row = leaderboardTable.insertRow();
            const rankCell = row.insertCell(0);
            const wordsCell = row.insertCell(1);
            const timeCell = row.insertCell(2);
            const wpmCell = row.insertCell(3);
            const accuracyCell = row.insertCell(4);
            const scoreCell = row.insertCell(5);
    
            rankCell.textContent = index + 1;
            wordsCell.textContent = entry.words;
            timeCell.textContent = entry.time.toFixed(2);
            wpmCell.textContent = entry.wpm;
            accuracyCell.textContent = entry.accuracy + "%";
            scoreCell.textContent = entry.score.toFixed(2);
    //bonus:
            if (index === 0) {
                row.style.color = "gold"; //first place
            } else if (index === 1) {
                row.style.color = "silver"; // Second place
            } else if (index === 2) {
                row.style.color = "peru"; // Third place
            }
        });
    }
    
    
    
    startGame();

    // Start the game when the "Start" button is clicked
    startButton.addEventListener("click", startGame);

    // Allow starting the game with the Enter key
    document.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            startGame();
        }
    });

    
    inputElement.addEventListener("input", checkInput);
    displayLeaderboard();
});


   