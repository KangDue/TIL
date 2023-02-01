importScripts('https://www.gstatic.com/firebasejs/5.0.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/5.0.0/firebase-messaging.js');
// Initialize Firebase
let firebaseConfig = {
    apiKey: "AIzaSyDvJejVFY-wCtazPPaTpEkcoKhoabfocDI",
    authDomain: "teak-environs-367508.firebaseapp.com",
    projectId: "teak-environs-367508",
    storageBucket: "teak-environs-367508.appspot.com",
    messagingSenderId: "850798980873",
    appId: "1:850798980873:web:5740cd25ae257345792dd8"
};
firebase.initializeApp(firebaseConfig);
const messaging = firebase.messaging();