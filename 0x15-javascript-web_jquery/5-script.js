//  adds a <li> element to a list when the user clicks on the tag DIV#add_item

$('div#red_header').click(function () {
    li_element = '<li>Item</li>';
    $('header').append(li_element);
});
