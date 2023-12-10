import axios from 'axios';

function getCSRFToken() {
    const csrfCookie = document.cookie
        .split('; ')
        .find(cookie => cookie.startsWith('csrftoken='));
    if (csrfCookie) {
        console.log(csrfCookie);
        return csrfCookie.split('=')[1];
    }
    return null;
}

const csrftoken = getCSRFToken();  // Implement a function to get the CSRF token


const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/timetable/api/',  // Update with your Django API endpoint
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken,
  },
});

export default api;