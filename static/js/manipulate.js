var savedName = localStorage.getItem("savedName")
console.log(savedName, savedName)
if (savedName) {
    $("#userInfo").hide()
}
$(document).ready(function() {
    console.log("fffff")
        // Your web app's Firebase configuration
        // For Firebase JS SDK v7.20.0 and later, measurementId is optional
    var firebaseConfig = {
        apiKey: "AIzaSyA6B2WbaEKlLwR1BVX5oUK7CqyxnyzMf-A",
        authDomain: "pidgin-english.firebaseapp.com",
        databaseURL: "https://pidgin-english-default-rtdb.firebaseio.com",
        projectId: "pidgin-english",
        storageBucket: "pidgin-english.appspot.com",
        messagingSenderId: "669992210576",
        appId: "1:669992210576:web:61e815c3530eb0706e4815",
        measurementId: "G-XZFY9QGPJT"
    };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    firebase.analytics();

    var firestore = firebase.firestore();




    $("#nextWord").click((e) => {
        e.preventDefault();
        console.log("Ok na");
        location.reload();
    })

    $("#submitWord").click((e) => {
        e.preventDefault();
        console.log("Ok na");
        var name = localStorage.getItem("savedName") || $("#user").val();
        var ip = $("#ip").val();
        var english = $("#from").val();
        var pidgin = $("#translated").val();

        var newTranslate = {
            english,
            pidgin,
            "user": {
                name,
                ip
            },
            date: new Date().toJSON().slice(0, 10).replace(/-/g, '-')
        }

        firestore.collection("translate").doc().set({
            newTranslate
        }, { merge: false }).then(() => {
            console.log("Translate Saved");
            localStorage.setItem("savedName", name);
            location.reload();
        }).catch((e) => {
            console.log("Got an error" + e);
        })
        console.log(newTranslate, "--------")
            // location.reload();
    })
})