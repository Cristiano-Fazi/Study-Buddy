import { fetchYouTubeVideos, fetchPracticeProblems, fetchPreviousExams, fetchAIResponse } from '../services/data-service.js';

document.addEventListener("DOMContentLoaded", function () {
    const checkedBoxes = JSON.parse(localStorage.getItem("checkedBoxes")) || [];
    const videoLength = localStorage.getItem("videoLength");
    const year = localStorage.getItem("year");
    const info = localStorage.getItem("info");

    console.log("Loaded Data:");
    console.log(checkedBoxes, videoLength, year, info);

    const resultsContainer = document.querySelector(".form_result");

    if (checkedBoxes.includes("video")) {
        fetchYouTubeVideos(info, year, 5, videoLength).then((response) => {
            let vid = document.createElement("h3");
            vid.textContent = "Videos";
            resultsContainer.appendChild(vid);
            resultsContainer.appendChild(document.createElement("br"));

            for (let i = 0; i < 5; i++) {
                let a = document.createElement("a");
                a.href = response[i].url;
                a.textContent = response[i].title;
                resultsContainer.appendChild(a);
                resultsContainer.appendChild(document.createElement("br"));
            }
        });
    }

    if (checkedBoxes.includes("exams")) {
        fetchPreviousExams(info, year).then((response) => {
            let exams = document.createElement("h3");
            exams.textContent = "Exams";
            resultsContainer.appendChild(exams);
            resultsContainer.appendChild(document.createElement("br"));

            for (let i = 0; i < 5; i++) {
                let a = document.createElement("a");
                a.href = response[i].url;
                a.textContent = response[i].title;
                resultsContainer.appendChild(a);
                resultsContainer.appendChild(document.createElement("br"));
            }
        });
    }

    if (checkedBoxes.includes("practice-problems")) {
        fetchPracticeProblems(info, year).then((response) => {
            let practice_problems = document.createElement("h3");
        practice_problems.textContent = "Practice Problems";
        resultsContainer.appendChild(practice_problems);
        resultsContainer.appendChild(document.createElement("br"));
            for (let i = 0; i < 5; i++) {
                let a = document.createElement("a");
                a.href = response[i].url;
                a.textContent = response[i].title;
                resultsContainer.appendChild(a);
                resultsContainer.appendChild(document.createElement("br"));
            }
        });
    }

    console.log("Chat were in")
    fetchAIResponse(info).then((response) => {
        console.log(response);
        console.log("Chat we out")
    });
});
