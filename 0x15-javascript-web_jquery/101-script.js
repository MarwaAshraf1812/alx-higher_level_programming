//adds, removes and clears LI elements from a list when the user clicks

$('DIV#add_item').click(function () {
    $('ui.my_list').append('<li>Item</li>');
});
$('DIV#remove_item').click(function () {
    $('ui.my_list').remove();
});

$('DIV#clear_list').click(function () {
    $('ui.my_list').empty();
});
