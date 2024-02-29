// fetches and lists the title for all movies by using URL

let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function(data) {
    var films = data.results;
    for (let film in films) {
        $('ul#list_movies').append(`<li>${film.title}</li>`);
    }
});
