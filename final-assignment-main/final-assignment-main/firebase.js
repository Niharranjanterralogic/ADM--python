import firebase from "firebase/app";
import "firebase/auth";
import "firebase/database";
import "firebase/storage";

const app = firebase.initializeApp({
  /* apiKey: "AIzaSyAVSGHJAW60Oh_7ucsaFybJnoaigA1Z5g0",
  authDomain: "reacthttp-e96d3.firebaseapp.com",
  databaseURL:
    "https://reacthttp-e96d3-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "reacthttp-e96d3",
  storageBucket: "reacthttp-e96d3.appspot.com",
  messagingSenderId: "467534846324",
  appId: "1:467534846324:web:ed2a82664009682d233421",*/
  apiKey: "AIzaSyC90_VmlmcKY8a4R8M6Vdg9cicuVYxOonM",
  authDomain: "database-60c4a.firebaseapp.com",
  databaseURL: "https://database-60c4a-default-rtdb.firebaseio.com",
  projectId: "database-60c4a",
  storageBucket: "database-60c4a.appspot.com",
  messagingSenderId: "1049626850172",
  appId: "1:1049626850172:web:300c9fc670de09ccf22af9",
});

export const auth = app.auth();
export const storage = firebase.storage();

export default app;
