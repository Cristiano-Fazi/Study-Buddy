import { fetchYouTubeVideos, fetchPracticeProblems, fetchPreviousExams } from '../services/data-service.js';

document.getElementById("request").addEventListener("submit", function(event){
    event.preventDefault();
    let checkedBoxes = [];

    if(document.getElementById("videos").checked){
        checkedBoxes.push("video");
    }
    if(document.getElementById("exams").checked){
        checkedBoxes.push("exams");
    }
    if(document.getElementById("practice-problems").checked){
        checkedBoxes.push("practice-problems");
    }
    
    //slidebar values if applicable
    let videoLength = /*document.getElementById("video_slide").style.display === "block" ? */ document.getElementById("video_length").value /*: "N/A"*/;
    let year = /*document.getElementById("publish_slide").style.display === "block" ? */ document.getElementById("publish_date").value /*: "N/A"*/;

    let info = document.getElementById("search").value;

    console.log(videoLength);
    console.log(year);
    console.log(checkedBoxes);
    console.log(info);

    if(checkedBoxes.includes("video")){
        fetchYouTubeVideos(info, year).then((response) =>
            console.log(response)
        );
    }

    if(checkedBoxes.includes("exams")){
        fetchPreviousExams(info, year).then((response) =>
            console.log(response)
        );
    }

    if(checkedBoxes.includes("practice-problems")){
        fetchPracticeProblems(info, year).then((response) =>
            console.log(response)
        );
    }
})
