$(document).ready(function(){
    confib();
});
function confib(){
    $("#buscar form").ajaxForm({
        beforeSubmit:function(){
            cargando();
            alert("Cargando requerimientos");
        },
        success: function (data) {
            cargando();
            $("#buscar").html(data);
        },
        error: function () {
            cargando();
            alert("Problemas en el servidor");
        }
    });
}

confib();