const url = "https://swapi-api.hbtn.io/api/people/5/?format=json"
$.get(url, function(body) {
    let name = body["name"];
    $("#character").html(name)
});