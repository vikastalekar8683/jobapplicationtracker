import axios from 'axios';

const baseURL = import.meta.env.PROD ? '/api' : 'http://localhost:8000';

const instance = axios.create({
    baseURL: baseURL,
    timeout: 10000,
});

export default instance;
