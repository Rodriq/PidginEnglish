$("input[type='radio']").click(function() {
    var sim = $("input[type='radio']:checked").val();
    var id = $("#_id").val();
    //alert(sim);
    if (sim <= 2) {
        $('.myratings').css('color', 'red');
        $(".myratings").text(sim);
        $('#displayUpdateModal').modal('show');
    } else if (sim <= 3) {
        $('.myratings').css('color', 'orange');
        $(".myratings").text(sim);
        rateTranslate(id, sim)

    } else {
        $('.myratings').css('color', 'green');
        $(".myratings").text(sim);
        rateTranslate(id, sim)
    }

});


function rateTranslate(id, rating) {
    var getUrl = window.location;
    var baseUrl = getUrl.protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1].split("rate", "");
    var requestUrl = baseUrl + "rate_translate"

    console.log(id, rating, requestUrl);

    // var client = new HttpClient();
    // client.get(`${requestUrl}?id=${id}&rating=${rating}`, function(response) {
    //     console.log(response.data);
    // });
    window.blur()

    $.get(requestUrl, { id, rating }, function(data) {
        // alert('page content: ' + data);
        window.location.reload()
    });

}

updateTranslate = (id, translate) => {
    var getUrl = window.location;
    var baseUrl = getUrl.protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1].split("rate", "");
    var requestUrl = baseUrl + "rate_translate"

    $.get(
        requestUrl, { paramOne: 1, paramX: 'abc' },
        function(data) {
            alert('page content: ' + data);
        }
    );
}