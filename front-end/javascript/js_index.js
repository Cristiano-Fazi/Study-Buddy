//tasks:
/*
when clicking a checkbox, the choices come up: for video: length, year
for the rest just year.
do it for each checkbox

when you press search, get all the infromation and put it like in an array or smt 
*/

const videoCheckbox = document.getElementById('videos');
const sliderWrapper = document.querySelector('.slider-wrapper');
const slider = document.getElementById('slider-range');
const yearDisplay = document.getElementById('year-display');
const tooltip = document.getElementById('slider-tooltip');

// Toggle visibility of slider when the "videos" checkbox is clicked
videoCheckbox.addEventListener('change', function () {
  sliderWrapper.style.visibility = videoCheckbox.checked ? 'visible' : 'hidden';
  
  // Reset the tooltip and slider value when the checkbox is unchecked
  if (!videoCheckbox.checked) {
    tooltip.style.visibility = 'hidden';
    slider.value = 2025;
    yearDisplay.textContent = '2025';
  }
});

// Show tooltip and update year when slider is moved
slider.addEventListener('input', function () {
  const yearValue = slider.value;
  yearDisplay.textContent = yearValue;
  
  if (videoCheckbox.checked) {
    tooltip.textContent = yearValue;
    tooltip.style.visibility = 'visible';
    tooltip.style.left = `calc(${(slider.value - slider.min) / (slider.max - slider.min) * 100}% - 20px)`;
  }
});

// Hide tooltip when mouse leaves slider
slider.addEventListener('mouseleave', function () {
  if (!videoCheckbox.checked) {
    tooltip.style.visibility = 'hidden';
  }
});


/*
<input type="range" min="1" max="100" value="50"></input>
*/