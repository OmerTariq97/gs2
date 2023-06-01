// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDWRsJY1s3INaXOlfWKZ8rhOAo_BpuicY8",
  authDomain: "testproject-61ca2.firebaseapp.com",
  projectId: "testproject-61ca2",
  storageBucket: "testproject-61ca2.appspot.com",
  messagingSenderId: "710261833852",
  appId: "1:710261833852:web:8fe10b425f6bb399eec9f9",
  measurementId: "G-VG1EN1FHE7"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);