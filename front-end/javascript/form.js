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

    const resultsContainer = document.querySelector(".form_result");

    if(checkedBoxes.includes("video")){
        let vid = document.createElement("h3");
        vid.textContent = "Videos";
        resultsContainer.appendChild(vid);
        resultContainer.appendChild(document.createElement("br"));

        fetchYouTubeVideos(info, year).then((response) =>{
            //make a for loop to go through all the results and print them a certain way

            //write video using p or wtv
        for (let i = 0; i < 5; i++) {
            console.log(response[i]);
        
            let a = document.createElement("a");
            a.href = response[i].url; //video link
            a.textContent = response[i].title; //video name

            resultsContainer.appendChild(a);
            CSSContainerRule.appendChild(document.createElement("br"));
          }
            
        });
    }
//add like video, exams, lectures before eveything, put it in the if checkbox includes
    if(checkedBoxes.includes("exams")){

        let exams = document.createElement("h3");
        exams.textContent = "Exams";
        resultsContainer.appendChild(exams);
        resultContainer.appendChild(document.createElement("br"));

        fetchPreviousExams(info, year).then((response) => {         
            console.log(response)
            for (let i = 0; i < 5; i++) {
                console.log(response[i]);
            
                let a = document.createElement("a");
                a.href = response[i].url; 
                a.textContent = response[i].title; 
    
                resultsContainer.appendChild(a);
                CSSContainerRule.appendChild(document.createElement("br"));
              }



        }
        );
    }

    if(checkedBoxes.includes("practice-problems")){

        let lecture = document.createElement("h3");
        lecture.textContent = "Lectures";
        resultsContainer.appendChild(lecture);
        resultContainer.appendChild(document.createElement("br"));

        fetchPracticeProblems(info, year).then((response) => {
            console.log(response)

            for (let i = 0; i < 5; i++) {
                console.log(response[i]);
            
                let a = document.createElement("a");
                a.href = response[i].url; 
                a.textContent = response[i].title; 
    
                resultsContainer.appendChild(a);
                resultsContainer.appendChild(document.createElement("br"));
              }

        }
        );
    }
})
