// fetches the character name from URL

let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function(data) {
    var name = data.name;
    $('div#character').text(name);
});
