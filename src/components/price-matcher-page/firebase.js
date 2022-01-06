// Import the functions you need from the SDKs you need
import firebase from 'firebase/app'
import { initializeApp } from 'firebase/app';
import { getFirestore } from "firebase/firestore";
// import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBhBTfPb9IthjHOwptAXuhoo47v_drBbQA",
  authDomain: "pricematch-326403.firebaseapp.com",
  projectId: "pricematch-326403",
  storageBucket: "pricematch-326403.appspot.com",
  messagingSenderId: "917502722224",
  appId: "1:917502722224:web:7bc8438944b65e9247bb75"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export default getFirestore();
export { app };
// const storageVariable = storage();

// export { 
//   storageVariable 
//  };