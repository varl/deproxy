
var browser = $('#browser'),
    addressbar = $('#address-bar'),
    tot_height = window.innerHeight,
    tot_width = window.innerWidth;

    console.log(tot_height +" "+ tot_width);

    browser.width(tot_width-16);
    browser.height(tot_height-16);

    addressbar.width(tot_width-20);
