if ('serviceWorker' in navigator) {
    navigator.serviceWorker
        .register('../service-worker.js')
        .then(function(registration) {
            console.log('Service Worker Registered!');
            return registration;
        })
        .catch(function(err) {
            console.error('Unable to register service worker.', err);
        });
}

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

$("#share").attr('href', `whatsapp://send?text=http://pidgin-english.tech`);

$(document).ready(function() {
    console.log("fffff")

})

// Initiate Service worker button

let deferredInstallPrompt = null;
const installButton = document.getElementById('installButton');
installButton.addEventListener('click', installPWA);

window.addEventListener('beforeinstallprompt', saveBeforeInstallPromptEvent);

function saveBeforeInstallPromptEvent(evt) {
    deferredInstallPrompt = evt;
    // installButton.removeAttribute('hidden');
    $('#installModal').modal('show');

}

function installPWA(evt) {
    deferredInstallPrompt.prompt();
    evt.srcElement.setAttribute('hidden', true);
    deferredInstallPrompt.userChoice
        .then((choice) => {
            if (choice.outcome === 'accepted') {
                console.log('User accepted the A2HS prompt', choice);
            } else {
                console.log('User dismissed the A2HS prompt', choice);
            }
            deferredInstallPrompt = null;
        });
}

window.addEventListener('appinstalled', logAppInstalled);

function logAppInstalled(evt) {
    console.log('App was installed.', evt);
}