// fetches  and displays the value of hello from that 
// fetch in the HTML tag DIV#hello

let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function(data) {
    $('DIV#hello').text(data.hello); 
});
