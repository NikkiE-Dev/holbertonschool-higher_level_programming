const url = "https://swapi-api.hbtn.io/api/films/?format=json";
$.get(url, function(body) {
    let titles = body["results"];
    let movie_list = $("#list_movies");
    titles.forEach(element => {
        movie_list.append("<li>" + element["title"] + "<li>");
    });
});
