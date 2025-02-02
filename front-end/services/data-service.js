const BASE_URL = 'http://127.0.0.1:8000/'; // Adjust base URL if necessary

// Function to fetch YouTube videos by subject
export async function fetchYouTubeVideos(subject, yearsAgo = null, maxResults = null) {
    let url = `${BASE_URL}youtube/${subject}/`;

    if (yearsAgo !== null && maxResults !== null) {
        url = `${BASE_URL}youtube/${subject}/${yearsAgo}/${maxResults}/`;
    } else if (yearsAgo !== null) {
        url = `${BASE_URL}youtube/${subject}/${yearsAgo}/`;
    }

    try {
        console.log(url);
        const response = await fetch(url);
        const data = await response.json();
        return data; // Return data for further use
    } catch (error) {
        console.error("Error fetching YouTube videos:", error);
        throw error; // Handle error or rethrow
    }
}

// Function to fetch practice problems by subject
export async function fetchPracticeProblems(subject, yearsAgo = null, maxResults = null) {
    let url = `${BASE_URL}practice/${subject}/`;

    if (yearsAgo !== null && maxResults !== null) {
        url = `${BASE_URL}practice/${subject}/${yearsAgo}/${maxResults}/`;
    } else if (yearsAgo !== null) {
        url = `${BASE_URL}practice/${subject}/${yearsAgo}/`;
    }

    try {
        const response = await fetch(url);
        const data = await response.json();
        return data; // Return data for further use
    } catch (error) {
        console.error("Error fetching practice problems:", error);
        throw error; // Handle error or rethrow
    }
}

// Function to fetch exams by subject
export async function fetchPreviousExams(subject, yearsAgo = null, maxResults = null) {
    let url = `${BASE_URL}exam/${subject}/`;

    if (yearsAgo !== null && maxResults !== null) {
        url = `${BASE_URL}exam/${subject}/${yearsAgo}/${maxResults}/`;
    } else if (yearsAgo !== null) {
        url = `${BASE_URL}exam/${subject}/${yearsAgo}/`;
    }

    try {
        const response = await fetch(url);
        const data = await response.json();
        return data; // Return data for further use
    } catch (error) {
        console.error("Error fetching practice problems:", error);
        throw error; // Handle error or rethrow
    }
}