document.addEventListener('DOMContentLoaded', function () {
    about_menu_button = document.querySelector("#about_menu_button");
    how_menu_button = document.querySelector("#how_menu_button");
    about_menu_button_mobile = document.querySelector("#about_menu_button_mobile");
    how_menu_button_mobile = document.querySelector("#how_menu_button_mobile");

    about_menu_button.addEventListener("click", function (event) {
        event.preventDefault();
        document.querySelector('#about_section').scrollIntoView({
            behavior: 'smooth'
        });
    });

    how_menu_button.addEventListener("click", function (event) {
        event.preventDefault();
        document.querySelector('#how_it_works').scrollIntoView({
            behavior: 'smooth'
        });
    });

    about_menu_button_mobile.addEventListener("click", function (event) {
        event.preventDefault();
        document.querySelector('#about_section_mobile').scrollIntoView({
            behavior: 'smooth'
        });
    });

    how_menu_button_mobile.addEventListener("click", function (event) {
        event.preventDefault();
        document.querySelector('#how_it_works_mobile').scrollIntoView({
            behavior: 'smooth'
        });
    });
});