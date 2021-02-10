var savedName = localStorage.getItem("savedName")
console.log(savedName, savedName)
if (savedName) {
    $("#user").val(localStorage.getItem("savedName"))
}

$("#user").change(function() {
        console.log($("#user").val())
        localStorage.setItem("savedName", $("#user").val())
    })
$("#nextWord").click((e) => {
        e.preventDefault();
        console.log("Ok na");
        location.reload();
    })

$(document).ready(function() {
    console.log("fffff")

   

    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional

    // var firebaseConfig = {
    //     apiKey: "AIzaSyA6B2WbaEKlLwR1BVX5oUK7CqyxnyzMf-A",
    //     authDomain: "pidgin-english.firebaseapp.com",
    //     databaseURL: "https://pidgin-english-default-rtdb.firebaseio.com",
    //     projectId: "pidgin-english",
    //     storageBucket: "pidgin-english.appspot.com",
    //     messagingSenderId: "669992210576",
    //     appId: "1:669992210576:web:61e815c3530eb0706e4815",
    //     measurementId: "G-XZFY9QGPJT"
    // };

    // var firebaseConfig = {
    //     apiKey: "AIzaSyDtk4t5AluN7isQLj-85BP2h_daHQ8J6DU",
    //     authDomain: "pidgin2-cf71d.firebaseapp.com",
    //     projectId: "pidgin2-cf71d",
    //     storageBucket: "pidgin2-cf71d.appspot.com",
    //     messagingSenderId: "429649361416",
    //     appId: "1:429649361416:web:3defa3f8997b9a3640efbd",
    //     measurementId: "G-0V2VK7T99C"
    // };


    // var firebaseConfig = {
    //     apiKey: "AIzaSyAzEUsaGX3D-vCEf3ebZHUToTQQwC8t1YQ",
    //     authDomain: "pidginenglish-723a4.firebaseapp.com",
    //     projectId: "pidginenglish-723a4",
    //     storageBucket: "pidginenglish-723a4.appspot.com",
    //     messagingSenderId: "123668323740",
    //     appId: "1:123668323740:web:f51f875cdd8667b3d77c59",
    //     measurementId: "G-3J6D2CNC45"
    // };

    // // Initialize Firebase
    // firebase.initializeApp(firebaseConfig);
    // firebase.analytics();

    // var firestore = firebase.firestore();

    
    // $("#submitWord").click((e) => {
    //     if (pidgin = $("#translated").val()) {
    //         e.preventDefault();
    //         console.log("Ok na");
    //         var name = localStorage.getItem("savedName") || $("#user").val();
    //         var ip = $("#ip").val();
    //         var english = $("#from").val();
    //         var pidgin = $("#translated").val();

    //         var newTranslate = {
    //             english,
    //             pidgin,
    //             "user": {
    //                 name,
    //                 ip
    //             },
    //             date: new Date().toJSON().slice(0, 10).replace(/-/g, '-')
    //         }

    //         firestore.collection("translate1").doc().set(
    //             newTranslate, { merge: false }).then(() => {
    //             console.log("Translate Saved");
    //             localStorage.setItem("savedName", name);
    //             location.reload();

    //         }).catch((e) => {
    //             console.log("Got an error" + e);
    //         })
    //         console.log(newTranslate, "--------")

    //         // location.reload();
    //     }
    // })

    // var allUsers = []
    // var regUsers = []


    // if ($("#displayTranslate").is(":visible")) {
    //     firestore.collection("translate1").get().then((querySnapshot) => {
    //         querySnapshot.forEach((doc) => {
    //             console.log(JSON.stringify(doc.data()), "00000000000000")
    //             allUsers.push(JSON.stringify(doc.data().newTranslate) || JSON.stringify(doc.data()))
    //         })
    //         console.log(allUsers, "all users");

    //         allUsers.forEach(el => {
    //             console.log(JSON.parse(el), "88888888888888")
    //             regUsers.push(JSON.parse(el))
    //         })

    //         console.log(regUsers, "-----------s")
    //         regUsers.sort((a, b) => {
    //             return a.date - b.date
    //         });

    //         var i = 1
    //         regUsers.forEach(el2 => {
    //             $("#displayTranslate").append(
    //                 `<tr>
    //                 <td scope="row">${i}</td>
    //                 <td>${el2.english}</td>
    //                 <td>${el2.pidgin}</td>
    //                 <td>${el2.user.name || el2.user.ip.substring(0, 6) + "****"}</td>
    //                 </tr>`
    //             );
    //             i = i + 1
    //         })


    // })



    // }

    
})
$("#share").attr('href', `whatsapp://send?text=http://pidgin-english.tech`);
// firestore.collection("translate").get().then((querySnapshot) => {
//     querySnapshot.forEach((doc) => {
//         // $("#data").append(`<p>${doc.fname}</p>`)
//         // console.log(typeof(JSON.stringify(doc.data())))
//         // console.log(` ${JSON.stringify(doc.data())}`);
//         allUsers.push(JSON.stringify(doc.data()));
//     });
//     console.log(allUsers, "all users---")
//     allUsers.forEach(el => {
//         // console.log(JSON.parse(el).position)
//         regUsers.push(JSON.parse(el))
//         // $("#data").append(`<p>${JSON.parse(el).fname}</p>`)
//     })

//     regUsers.sort((a, b) => {
//         return a.date - b.date
//     });

//     console.log(regUsers, "reg users----")
//     var i = 1
//     regUsers.forEach(el => {
//         // console.log(JSON.parse(el).position)
//         $("#displayTranslate").append(
//             `<tr>
//                     <td>${i}</td>
//                     <td>${el.english}</td>
//                     <td>${el.pidgin}</td>
//                     <td>${el.user.name || el.user.ip}</td>
//                     </tr>`
//         );
//         i = i + 1
//     }
//     )