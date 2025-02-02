//tasks:
/*
when clicking a checkbox, the choices come up: for video: length, year
for the rest just year.
do it for each checkbox

when you press search, get all the infromation and put it like in an array or smt 
*/

/*
1. auto hide the bars  X
2. when any of the checkmarks are pressed then the publish date bar appears
3. when video is checked then length appears
4. display the value on the slider on the side
*/

const pub_slider = document.getElementById("publish_date")
const vid_slider = document.getElementById("video_length")

vid_slider.style.display = 'none'

const vid_check = document.getElementById("videos")
const exams_check = document.getElementById("exams")
const lect_note_check = document.getElementById("lecture_notes")


vid_check.addEventListener('change', function()
{
    if (this.checked) {
        vid_slider.style.display = 'initial'
    }
    else {
        vid_slider.style.display = 'none'
    }
})

