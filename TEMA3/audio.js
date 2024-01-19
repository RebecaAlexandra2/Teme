let sequence = [];
let userSequence = [];
let sounds = [];

document.addEventListener("DOMContentLoaded", function() {
    sounds = [document.getElementById("sound1"), 
              document.getElementById("sound2"), 
              document.getElementById("sound3"), 
              document.getElementById("sound4")];
});

function startGame() {
    sequence = [];
    userSequence = [];
    addSoundToSequence();
}

function addSoundToSequence() {
    const randomIndex = Math.floor(Math.random() * sounds.length);
    sequence.push(randomIndex);
    playSequence();
}

function playSequence() {
    let i = 0;
    const interval = setInterval(function() {
        playSound(sequence[i]);
        i++;
        if (i >= sequence.length) {
            clearInterval(interval);
        }
    }, 1000);

    userSequence = [];
}

function playSound(index) {
    sounds[index].play();
}

document.addEventListener("keydown", function(event) {
    const index = parseInt(event.key) - 1;
    if (index >= 0 && index < sounds.length) {
        playSound(index);
        userSequence.push(index);
        checkSequence();
    }
});

function checkSequence() {
    for (let i = 0; i < userSequence.length; i++) {
        if (userSequence[i] != sequence[i]) {
            document.getElementById("message").innerText = "Greșit! Încearcă din nou.";
            return;
        }
    }
    if (userSequence.length == sequence.length) {
        document.getElementById("message").innerText = "Corect! Următorul nivel.";
        addSoundToSequence();
    }
}
