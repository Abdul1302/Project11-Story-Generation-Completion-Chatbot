
/* Axios is a popular library for making HTTP requests 
in JS applications. */

import axios from "axios";

// making HTTP requests to a backend API in a JS application
const api = axios.create({

  /*the base URL in axios (or any HTTP request library) 
    acts like a starting address for your API requests. 
    It defines the root location of the backend server you're
    communicating with.*/

  baseURL: 'http://127.0.0.1:8000',
});

export default api;
