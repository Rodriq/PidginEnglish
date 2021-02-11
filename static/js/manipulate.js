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