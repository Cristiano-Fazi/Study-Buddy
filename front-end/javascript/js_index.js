//tasks:
/*
when clicking a checkbox, the choices come up: for video: length, year
for the rest just year.
do it for each checkbox

when you press search, get all the infromation and put it like in an array or smt 
*/

const pub_slider = document.getElementById("publish_date")
const vid_slider = document.getElementById("video_length")

vid_slider.style.display = 'none'
pub_slider.style.display = 'none'

const vid_check = document.getElementById("videos")
const exams_check = document.getElementById("exams")
const lect_note_check = document.getElementById("lecture_notes")

const checkboxes = document.querySelectorAll('input[type="checkbox"]');

updateElementVisibility()

vid_check.addEventListener('change', function()
{
    if (this.checked) {
        vid_slider.style.display = 'block'
        document.getElementById("vid_slide_num").style.display = "block"
        document.getElementById("vid_slide_num").textContent = vid_slider.value
    }
    else {
        vid_slider.style.display = 'none'
        document.getElementById("vid_slide_num").textContent = vid_slider.value
        document.getElementById("vid_slide_num").style.display = "none"
    }
    
})

function updateElementVisibility()
{
    const isAnyChecked = Array.from(checkboxes).some(checkbox => checkbox.checked)
    if (isAnyChecked) {
        pub_slider.style.display = "block";
        document.getElementById("pub_slide_num").style.display = "block"
        document.getElementById("pub_slide_num").textContent = pub_slider.value
    } else {
        pub_slider.style.display = "none";
        document.getElementById("pub_slide_num").textContent = pub_slider.value
        document.getElementById("pub_slide_num").style.display = "none"
    }
    if (vid_check.checked) {
        document.getElementById("vid_slide_num").style.display = "block"
        document.getElementById("vid_slide_num").textContent = vid_slider.value
    }
    else {
        document.getElementById("vid_slide_num").textContent = vid_slider.value
        document.getElementById("vid_slide_num").style.display = "none"
    }
}

checkboxes.forEach(checkbox => {
    checkbox.addEventListener("change", updateElementVisibility);
});

pub_slider.addEventListener("change", function() {
    document.getElementById("pub_slide_num").textContent = this.value
})
vid_slider.addEventListener("change", function() {
    document.getElementById("vid_slide_num").textContent = this.value
})
