import axios from 'axios';
 
const baseurl = "http://127.0.0.1:5000"

const mainRequest = axios.create({
    baseURL: baseurl+"/api/"
});

const bookRequest = axios.create({
    baseURL: baseurl+"/api/book/"
});

const storeRequest = axios.create({
    baseURL: baseurl+"/api/store/"
});

// user相關 api
// export const apiUserRegister = data => mainRequest.post('/' , data);
// export const apiUserLogin = data => mainRequest.post('/login' , data);
// export const apiUserLogout = data => mainRequest.get('/logout' , data);

// book相關 api
// export const apiGetBooks = () => bookRequest.get('/');
// export const apiGetBooksAmount = () => bookRequest.get('/amount');

// // store 相關 api
// export const apiGetStores = () =>storeRequest.get('/');
// export const apiGetStoresAmount = () =>storeRequest.get('/amount');