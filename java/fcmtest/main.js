// Initialize Firebase
var firebaseConfig = {
    apiKey: "AIzaSyDvJejVFY-wCtazPPaTpEkcoKhoabfocDI",
    authDomain: "teak-environs-367508.firebaseapp.com",
    projectId: "teak-environs-367508",
    storageBucket: "teak-environs-367508.appspot.com",
    messagingSenderId: "850798980873",
    appId: "1:850798980873:web:5740cd25ae257345792dd8"
  };
  firebase.initializeApp(firebaseConfig);
  
  // Get messaging object
  const messaging = firebase.messaging();
  

  document.getElementById("notify-button").addEventListener("click", function() {
    Notification.requestPermission().then(function(permission) {
      if (permission === "granted") {
        var notification = new Notification("Hello!", {
          body: "You have a new notification."
        });
      }
    });
  });

  // Request permission for notification
  messaging.requestPermission()
  .then(function() {
    console.log("Notification permission granted.");
    // Get token
    messaging.getToken()
    .then(function(currentToken) {
      if (currentToken) {
        console.log("Token: ", currentToken);
        document.getElementById("message").innerHTML = "Token: " + currentToken;
      } else {
        console.log("No Instance ID token available. Request permission to generate one.");
      }
    })
    .catch(function(err) {
      console.log("An error occurred while retrieving token. ", err);
    });
  })
  .catch(function(err) {
    console.log("Unable to get permission to notify.", err);
  });
  
  // Listen for incoming messages
  messaging.onMessage(function(payload) {
    console.log("Message received. ", payload);
    var notificationTitle = payload.notification.title;
    var notificationOptions = {
      body: payload.notification.body,
      icon: "/firebase-logo.png"
    };
    new Notification(notificationTitle, notificationOptions);
  });
  