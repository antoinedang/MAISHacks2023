const musicContainer = document.getElementById("music-container");
const playBtn = document.getElementById("play");
const prevBtn = document.getElementById("prev");
const nextBtn = document.getElementById("next");
const audio = document.getElementById("audio");
const progress = document.getElementById("progress");
const progressContainer = document.getElementById("progress-container");
const title = document.getElementById("title");
const cover = document.getElementById("cover");
// Songs Titles
const songs = ["lofi_1"];
// KeepTrack of song
let songIndex = 0;
// Initially load song details into DOM
loadSong(songs[songIndex]);
// Update song details
function loadSong(song) {
title.innerText = song;
audio.src = `./music/${song}.mp3`;
cover.src = `./images/${song}.jpg`;
}
// Play Song
function playSong() {
musicContainer.classList.add("play");
playBtn.querySelector("i.fa").classList.remove("fa-play");
playBtn.querySelector("i.fa").classList.add("fa-pause");
audio.play();
}
// Pause Song
function pauseSong() {
musicContainer.classList.remove("play");
playBtn.querySelector("i.fa").classList.add("fa-play");
playBtn.querySelector("i.fa").classList.remove("fa-pause");
audio.pause();
}
// Previous Song
function prevSong() {
songIndex--;
if (songIndex < 0) {
songIndex = songs.length - 1;
}
loadSong(songs[songIndex]);
playSong();
}
// Next Song
function nextSong() {
songIndex++;
if (songIndex > songs.length - 1) {
songIndex = 0;
}
loadSong(songs[songIndex]);
playSong();
}
// Update Progress bar
function updateProgress(e) {
const { duration, currentTime } = e.srcElement;
const progressPerCent = (currentTime / duration) * 100;
progress.style.width = `${progressPerCent}%`;
}
// Set Progress
function setProgress(e) {
const width = this.clientWidth;
const clickX = e.offsetX;
const duration = audio.duration;
audio.currentTime = (clickX / width) * duration;
}
// Event Listeners
playBtn.addEventListener("click", () => {
const isPlaying = musicContainer.classList.contains("play");
if (isPlaying) {
pauseSong();
} else {
playSong();
}
});
// Change Song
prevBtn.addEventListener("click", prevSong);
nextBtn.addEventListener("click", nextSong);
// Time/Song Update
audio.addEventListener("timeupdate", updateProgress);
// Click On progress Bar
progressContainer.addEventListener("click", setProgress);
// Song End
audio.addEventListener("ended", nextSong);

const textInput = document.getElementById('textInput');
const submitButton = document.getElementById('submitButton');
const output = document.getElementById('output');

submitButton.addEventListener('click', () => {
    const userInput = textInput.value;
    output.textContent = `You entered: ${userInput}`;

    const url = new URL('http://localhost:5000/playmidi');
    url.searchParams.append("primer", userInput);
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); 
        })
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });

});

const playPauseDropdownBtn = document.getElementById("play-pause-dropdown");
const songSelector = document.getElementById("song-selector");

// Update the loadSong function to load the selected song
function loadSelectedSong() {
  const selectedSong = songSelector.value;
  title.innerText = selectedSong;
  audio.src = `./music/${selectedSong}.mp3`;
  cover.src = `./images/${selectedSong}.jpg`;
}

// Play/Pause functionality for the new button
playPauseDropdownBtn.addEventListener("click", () => {
  if (audio.paused) {
    loadSelectedSong();
    playSong();
  } else {
    pauseSong();
  }
});

// Change song when an option is selected from the dropdown
songSelector.addEventListener("change", () => {
  if (!audio.paused) {
    // If a song is currently playing, pause it and load the new song
    pauseSong();
    loadSelectedSong();
    playSong();
  } else {
    // If no song is playing, simply load the new song
    loadSelectedSong();
  }
});
