

document.getElementById("request").addEventListener("submit", function(event){
    event.preventDefault();
    console.log('HIIIIIII :3')
    let checkedBoxes = [];

    if(document.getElementById("videos").checked){
        checkedBoxes.push("video");
    }
    if(document.getElementById("exams").checked){
        checkedBoxes.push("exams");
    }
    if(document.getElementById("lecture-notes").checked){
        checkedBoxes.push("lecture-notes");
    }
    
    //slidebar values if applicable
    let videoLength = /*document.getElementById("video_slide").style.display === "block" ? */ document.getElementById("video_length").value /*: "N/A"*/;
    let year = /*document.getElementById("publish_slide").style.display === "block" ? */ document.getElementById("publish_date").value /*: "N/A"*/;

    let info = document.getElementById("search").value;

    console.log(videoLength);
    console.log(year);
    console.log(checkedBoxes);
    console.log(info);

})


