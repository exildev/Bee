$(document).ready(function () {

    $("#login form").ajaxForm({
        success: function (data) {
            $('#login').addClass('anilog');
            window.setTimeout(function () {
                $('#login').addClass('irse');
            }, 1800);
            window.setTimeout(function () {
                $("body").html('');
                window.location='/';
            }, 1800);          
        },
        error: function () {
            alert("Contraseña incorrecta");
        }
    });
});
